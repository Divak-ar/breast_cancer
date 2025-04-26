import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
import joblib  

cancer_dataset = load_breast_cancer()
X = cancer_dataset.data
y = cancer_dataset.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5, stratify=y)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

xgb_classifier = XGBClassifier()
xgb_classifier.fit(X_train, y_train)

joblib.dump(xgb_classifier, "model/breast_cancer_model.pkl")
joblib.dump(sc, "model/scaler.pkl")

print("Model and scaler saved successfully!")
