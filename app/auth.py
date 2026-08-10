from flask import Blueprint, redirect, render_template, request, session

from app.config import Config
from app.models import (
    UsernameTakenError,
    create_user,
    update_password,
    user_prediction_count,
    verify_user,
)

auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            return render_template("signup.html", error="Username and password are required.")
        if len(password) < Config.MIN_PASSWORD_LENGTH:
            return render_template(
                "signup.html",
                error=f"Password must be at least {Config.MIN_PASSWORD_LENGTH} characters.",
            )

        try:
            create_user(username, password)
        except UsernameTakenError as e:
            return render_template("signup.html", error=str(e))

        return redirect("/login?signup=success")

    return render_template("signup.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = verify_user(username, password)

        if user:
            session["user"] = username
            return redirect("/")
        else:
            return render_template("login.html", error="Invalid username or password.")

    just_signed_up = request.args.get("signup") == "success"
    return render_template("login.html", just_signed_up=just_signed_up)


@auth.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


@auth.route("/profile", methods=["GET", "POST"])
def profile():
    if "user" not in session:
        return redirect("/login")

    message = None
    error = None

    if request.method == "POST":
        current_password = request.form.get("current_password", "")
        new_password = request.form.get("new_password", "")

        if not verify_user(session["user"], current_password):
            error = "Current password is incorrect."
        elif len(new_password) < Config.MIN_PASSWORD_LENGTH:
            error = f"New password must be at least {Config.MIN_PASSWORD_LENGTH} characters."
        else:
            update_password(session["user"], new_password)
            message = "Password updated successfully."

    prediction_count = user_prediction_count(session["user"])
    return render_template(
        "profile.html",
        message=message,
        error=error,
        prediction_count=prediction_count,
    )
