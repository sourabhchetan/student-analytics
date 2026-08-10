import os
import secrets

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass  # python-dotenv is optional; env vars can be set another way


class Config:
    """Central place for app configuration, pulled from environment
    variables so nothing sensitive is hardcoded in source.
    """

    # Falls back to a random key per-process if not set, so the app still
    # runs locally without a .env, but you should ALWAYS set a real
    # SECRET_KEY in production (sessions won't survive restarts otherwise).
    SECRET_KEY = os.environ.get("SECRET_KEY") or secrets.token_hex(32)

    MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")

    DEBUG = os.environ.get("FLASK_DEBUG", "false").lower() in ("1", "true", "yes")

    # Validation ranges used across forms and API input checks
    MIN_HOURS, MAX_HOURS = 0, 24
    MIN_ATTENDANCE, MAX_ATTENDANCE = 0, 100
    MIN_SLEEP, MAX_SLEEP = 0, 24
    MIN_MARKS, MAX_MARKS = 0, 100

    MIN_PASSWORD_LENGTH = 8
