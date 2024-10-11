
import streamlit as st
import pandas as pd
import math
from pathlib import Path
import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('heart_disease_model.pkl')

# Title for the app
st.title('Heart Disease Prediction App')

# Input fields for user data
age = st.number_input('Age', min_value=1, max_value=120, value=25)
sex = st.selectbox('Sex', ('Male', 'Female'))
cp = st.selectbox('Chest Pain Type', (0, 1, 2, 3))
trestbps = st.number_input('Resting Blood Pressure', min_value=80, max_value=200, value=120)
chol = st.number_input('Cholesterol', min_value=100, max_value=600, value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', (0, 1))
restecg = st.selectbox('Resting Electrocardiographic results', (0, 1, 2))
thalach = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)
exang = st.selectbox('Exercise Induced Angina', (0, 1))
oldpeak = st.number_input('ST depression induced by exercise relative to rest', min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox('Slope of the peak exercise ST segment', (0, 1, 2))
ca = st.selectbox('Number of major vessels colored by fluoroscopy', (0, 1, 2, 3, 4))
thal = st.selectbox('Thalassemia', (0, 1, 2, 3))

# Collect input data into an array
user_data = np.array([[age, 1 if sex == 'Male' else 0, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

# Prediction button
if st.button('Predict'):
    prediction = model.predict(user_data)
    if prediction == 1:
        st.success('You are at risk of heart disease.')
    else:
        st.success('You are not at risk of heart disease.')


