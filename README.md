# Breast Cancer Detection System Using Machine Learning

![Breast Cancer Detection](https://img.shields.io/badge/Healthcare-ML-brightgreen)
![Accuracy](https://img.shields.io/badge/Accuracy-90%25-blue)

A web application that leverages machine learning to detect breast cancer by analyzing medical data inputs and classifying cases as either benign or malignant with high accuracy.

## 📋 Project Overview

This system uses the Wisconsin Breast Cancer Dataset to train machine learning models that can distinguish between benign and malignant breast cancer cases. The application provides an easy-to-use interface for medical professionals to input patient data and receive instant predictions.

## ✨ Features

- **High Accuracy**: Achieves ~90% accuracy in cancer detection
- **Input Preprocessing**: Implements feature scaling for consistent model performance
- **User-friendly Interface**: Intuitive web application for medical data input
- **Automated Testing**: Includes Selenium-based testing for application functionality
- **Responsive Design**: Clean CSS styling for various device sizes

## 🧪 Dataset

The system is trained on the Wisconsin Breast Cancer Dataset, which contains 30 features computed from digitized images of fine needle aspirates (FNA) of breast mass. Features include:

- Radius, texture, perimeter, area, smoothness
- Compactness, concavity, concave points
- Symmetry, fractal dimension
- Mean, standard error, and "worst" values for each feature

The target variable is coded as:
- 0: Malignant
- 1: Benign

## 🔧 Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn
- **Data Processing**: NumPy, joblib for model persistence
- **Frontend**: HTML5, CSS3
- **Testing**: Selenium WebDriver for automated testing


### Folder Explanations

- **model/**: Stores the trained machine learning model and scaler for preprocessing.
- **static/**: Contains static files like CSS for frontend styling.
- **templates/**: Holds HTML templates for rendering web pages.
- **utils/**: Utility scripts, such as data preprocessing functions.
- **testing/**: Automated test scripts (e.g., Selenium) for end-to-end testing.
- **app.py**: Main Flask application entry point.
- **breast_cancer_dataframe.csv**: The dataset used for model training and evaluation.

## 🚀 Installation and Setup

```bash
# Clone the repository
git clone https://github.com/Divak-ar/Breast_Cancer.git

# Navigate to the project directory
cd breast_cancer

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

## 💻 Usage

1. Launch the web application using `python app.py`
2. Open your browser and go to `http://127.0.0.1:5000`
3. Enter patient data in the provided input fields
4. Click the "Predict" button to receive cancer classification 
5. The system will display whether the sample is likely benign or malignant

## 🔍 Testing

Automated testing using Selenium WebDriver is included to ensure the application works as expected:

```bash
# Run automated tests
python testing/test_app.py
```

The test script automatically:
- Launches the web application
- Inputs test data into the form fields 
- Submits the form and validates the prediction response
- Provides test results in the console output