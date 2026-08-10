import os
import pickle

import numpy as np
import pandas as pd

_MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "model.pkl")

with open(_MODEL_PATH, "rb") as f:
    _loaded = pickle.load(f)

# Support both the new {"model", "features"} format and the old raw-model
# pickle, so this doesn't break if someone hasn't retrained yet.
if isinstance(_loaded, dict) and "model" in _loaded:
    model = _loaded["model"]
    FEATURES = _loaded["features"]
else:
    model = _loaded
    FEATURES = ["hours_study", "attendance", "sleep_hours", "previous_marks"]


def predict_marks(data):
    """data: list of feature values in FEATURES order."""
    features = pd.DataFrame([data], columns=FEATURES)
    prediction = model.predict(features)[0]
    return round(float(np.clip(prediction, 0, 100)), 2)


def study_hours_recommendation(hours, attendance, sleep, prev_marks, extra_hours=2):
    """Simple what-if: how much would `extra_hours` more study change the
    prediction? Gives students something actionable instead of a bare
    number.
    """
    current = predict_marks([hours, attendance, sleep, prev_marks])
    improved = predict_marks([hours + extra_hours, attendance, sleep, prev_marks])
    return {
        "current": current,
        "improved": improved,
        "gain": round(improved - current, 2),
        "extra_hours": extra_hours,
    }
