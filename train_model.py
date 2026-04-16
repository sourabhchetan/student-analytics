import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

# Create models folder if not exists
os.makedirs("models", exist_ok=True)

# Sample dataset
data = {
    "hours_study": [1,2,3,4,5,6,7,8],
    "attendance": [50,60,65,70,75,80,90,95],
    "sleep_hours": [4,5,6,6,7,7,8,8],
    "previous_marks": [30,40,45,50,55,60,70,80],
    "marks": [35,40,50,55,65,70,80,90]
}

df = pd.DataFrame(data)

X = df.drop("marks", axis=1)
y = df["marks"]

model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

# Save model
pickle.dump(model, open("models/model.pkl", "wb"))

print("✅ Model created successfully!")