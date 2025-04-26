from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("model/breast_cancer_model.pkl")
scaler = joblib.load("model/scaler.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            input_features = [float(x) for x in request.form.values()]
            input_features = np.array(input_features).reshape(1, -1)
            
            input_features_scaled = scaler.transform(input_features)


            prediction = model.predict(input_features_scaled)[0]
            result = "Benign (No Cancer)" if prediction == 1 else "Malignant (Cancer Detected)"
            return render_template("result.html", result=result)

        except Exception as e:
            return render_template("result.html", result="Error processing input!")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
