from flask import Blueprint, render_template, request, jsonify, session, redirect
from app.model import predict_marks
from app.db import collection
from datetime import datetime

main = Blueprint("main", __name__)

# ✅ PROTECTED HOME ROUTE
@main.route("/")
def home():
    if "user" not in session:
        return redirect("/login")
    return render_template("index.html")


# ✅ PREDICT ROUTE
@main.route("/predict", methods=["POST"])
def predict():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json

    # Convert to numeric
    hours = float(data["hours"])
    attendance = float(data["attendance"])
    sleep = float(data["sleep"])
    prev_marks = float(data["prev_marks"])

    # Predict
    prediction = predict_marks([
        hours,
        attendance,
        sleep,
        prev_marks
    ])

    # Store in MongoDB
    collection.insert_one({
        "user": session["user"],   # ✅ user tracking
        "hours": hours,
        "attendance": attendance,
        "sleep": sleep,
        "previous_marks": prev_marks,
        "prediction": prediction,
        "time": datetime.now()
    })

    return jsonify({"prediction": prediction})


# ✅ ANALYTICS ROUTE
@main.route("/analytics")
def analytics():
    if "user" not in session:
        return redirect("/login")

    data = list(collection.find(
        {"user": session["user"]},
        {"_id": 0}
    ))

    return render_template("analytics.html", data=data)