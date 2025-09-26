import streamlit as st
import joblib
import numpy as np

st.title('Titanic Survival Predictor')

# Use absolute path to your model
model = joblib.load(r'D:\best_random_forest.joblib')  # note the r'' raw string for Windows path

st.info('Model loaded successfully! Now you can make predictions.')

pclass = st.selectbox('Pclass', [1,2,3], index=2)
sex = st.selectbox('Sex', ['male','female'])
age = st.slider('Age', 0.42, 80.0, 30.0)
sibsp = st.slider('SibSp', 0, 8, 0)
parch = st.slider('Parch', 0, 6, 0)
fare = st.number_input('Fare', min_value=0.0, value=32.0)
embarked = st.selectbox('Embarked', ['C','Q','S'])

if st.button('Predict'):
    # For now, just a demo output
    st.write('This is a demo. Preprocessing must match training to predict correctly.')
    # Example: st.write('Prediction: Survived') if pred[0]==1 else 'Did not survive'

st.markdown('**Note:** Ensure preprocessing steps (scaler & encoding) are applied before making real predictions.')
