"""
Trains the marks-prediction model.

The original version trained on 8 hand-typed rows, which meant the model
could not generalize at all — it was memorizing, not learning. This
version generates a larger, noisier synthetic dataset that follows a
plausible real-world relationship (more study/attendance/sleep and a
higher previous score tend to raise marks, but with realistic scatter),
then reports held-out accuracy so you know how much to trust it.

Swap `generate_synthetic_dataset()` for a real CSV of student records
(pd.read_csv(...)) as soon as you have one — synthetic data is a
placeholder, not a destination.
"""
import os
import pickle

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

FEATURE_ORDER = ["hours_study", "attendance", "sleep_hours", "previous_marks"]


def generate_synthetic_dataset(n=400, seed=42):
    rng = np.random.default_rng(seed)

    hours_study = rng.uniform(0, 10, n)
    attendance = rng.uniform(40, 100, n)
    sleep_hours = rng.uniform(3, 10, n)
    previous_marks = rng.uniform(20, 95, n)

    # A plausible weighted relationship, plus noise so it isn't a
    # perfectly learnable straight line (real students aren't either).
    marks = (
        0.35 * previous_marks
        + 3.2 * hours_study
        + 0.28 * attendance
        - 1.5 * np.abs(sleep_hours - 7.5)  # too little/too much sleep both hurt
        + rng.normal(0, 6, n)
    )
    marks = np.clip(marks, 0, 100)

    return pd.DataFrame(
        {
            "hours_study": hours_study,
            "attendance": attendance,
            "sleep_hours": sleep_hours,
            "previous_marks": previous_marks,
            "marks": marks,
        }
    )


def main():
    os.makedirs("models", exist_ok=True)

    df = generate_synthetic_dataset()
    X = df[FEATURE_ORDER]
    y = df["marks"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=200, max_depth=8, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    with open("models/model.pkl", "wb") as f:
        pickle.dump({"model": model, "features": FEATURE_ORDER}, f)

    print("Model trained and saved to models/model.pkl")
    print(f"Held-out MAE: {mae:.2f} marks")
    print(f"Held-out R^2: {r2:.3f}")


if __name__ == "__main__":
    main()
