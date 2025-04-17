import streamlit as st
import joblib
import pandas as pd
from utils.feature_extractor import extract_features

# Load model
model = joblib.load("model/xgb_model.pkl")

# Streamlit UI
st.title("🔐 Malicious URL Detector")
st.subheader("Enter a URL to check if it's malicious")

url = st.text_input("Enter a URL:")

if st.button("Check URL"):
    if url:
        features = extract_features(url)
        df = pd.DataFrame([features])
        prediction = model.predict(df)[0]
        label = "🟢 Benign" if prediction == 0 else "🔴 Malicious"
        st.success(f"Prediction: {label}")
    else:
        st.warning("Please enter a URL.")
