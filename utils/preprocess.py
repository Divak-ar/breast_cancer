import numpy as np
import joblib

# Load the saved scaler
scaler = joblib.load("model/scaler.pkl")

def preprocess_input(input_data):
    input_array = np.array(input_data).reshape(1, -1)
    return scaler.transform(input_array)
