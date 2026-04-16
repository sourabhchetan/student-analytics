import pickle
import numpy as np

model = pickle.load(open("models/model.pkl", "rb"))

def predict_marks(data):
    features = np.array([data])
    prediction = model.predict(features)[0]
    return round(prediction, 2)
