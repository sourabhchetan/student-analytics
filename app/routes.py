import csv
import io
from datetime import datetime

from bson import ObjectId
from flask import (
    Blueprint,
    Response,
    jsonify,
    redirect,
    render_template,
    request,
    session,
)

from app.config import Config
from app.db import collection
from app.model import predict_marks, study_hours_recommendation

main = Blueprint("main", __name__)


def _require_login():
    return "user" not in session


def _validate_predict_input(data):
    """Returns (values_dict, error_message). error_message is None if valid."""
    required = ["hours", "attendance", "sleep", "prev_marks"]
    for field in required:
        if field not in data or data[field] in ("", None):
            return None, f"Missing field: {field}"

    try:
        hours = float(data["hours"])
        attendance = float(data["attendance"])
        sleep = float(data["sleep"])
        prev_marks = float(data["prev_marks"])
    except (TypeError, ValueError):
        return None, "All fields must be numbers."

    checks = [
        (hours, Config.MIN_HOURS, Config.MAX_HOURS, "Study hours"),
        (attendance, Config.MIN_ATTENDANCE, Config.MAX_ATTENDANCE, "Attendance"),
        (sleep, Config.MIN_SLEEP, Config.MAX_SLEEP, "Sleep hours"),
        (prev_marks, Config.MIN_MARKS, Config.MAX_MARKS, "Previous marks"),
    ]
    for value, lo, hi, label in checks:
        if not (lo <= value <= hi):
            return None, f"{label} must be between {lo} and {hi}."

    return {
        "hours": hours,
        "attendance": attendance,
        "sleep": sleep,
        "prev_marks": prev_marks,
    }, None


@main.route("/")
def home():
    if _require_login():
        return redirect("/login")
    return render_template("index.html")


@main.route("/predict", methods=["POST"])
def predict():
    if _require_login():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json(silent=True) or {}
    values, error = _validate_predict_input(data)
    if error:
        return jsonify({"error": error}), 400

    prediction = predict_marks(
        [values["hours"], values["attendance"], values["sleep"], values["prev_marks"]]
    )
    recommendation = study_hours_recommendation(
        values["hours"], values["attendance"], values["sleep"], values["prev_marks"]
    )

    collection.insert_one(
        {
            "user": session["user"],
            "hours": values["hours"],
            "attendance": values["attendance"],
            "sleep": values["sleep"],
            "previous_marks": values["prev_marks"],
            "prediction": prediction,
            "time": datetime.now(),
        }
    )

    return jsonify({"prediction": prediction, "recommendation": recommendation})


@main.route("/analytics")
def analytics():
    if _require_login():
        return redirect("/login")

    data = list(collection.find({"user": session["user"]}))
    for row in data:
        row["_id"] = str(row["_id"])
        if isinstance(row.get("time"), datetime):
            row["time"] = row["time"].isoformat()

    # Class-average comparison: how does this student stack up against
    # everyone else who has made a prediction?
    all_predictions = [d["prediction"] for d in collection.find({}, {"prediction": 1})]
    class_avg = round(sum(all_predictions) / len(all_predictions), 2) if all_predictions else None

    return render_template("analytics.html", data=data, class_avg=class_avg)


@main.route("/history/<entry_id>", methods=["DELETE"])
def delete_history(entry_id):
    if _require_login():
        return jsonify({"error": "Unauthorized"}), 401
    try:
        oid = ObjectId(entry_id)
    except Exception:
        return jsonify({"error": "Invalid id"}), 400

    result = collection.delete_one({"_id": oid, "user": session["user"]})
    if result.deleted_count == 0:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"success": True})


@main.route("/export")
def export_csv():
    if _require_login():
        return redirect("/login")

    data = list(collection.find({"user": session["user"]}, {"_id": 0}))
    output = io.StringIO()
    fieldnames = ["time", "hours", "attendance", "sleep", "previous_marks", "prediction"]
    writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    for row in data:
        if isinstance(row.get("time"), datetime):
            row["time"] = row["time"].isoformat()
        writer.writerow(row)

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=predictions.csv"},
    )
