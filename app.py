import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Page config
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="centered"
)

# Title
st.title("Customer Churn Predictor")
st.markdown("Predict whether a customer will churn based on their account details.")

# Input fields
st.header("Customer Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    phone_service = st.selectbox("Phone Service", ["No", "Yes"])
    mulitple_lines = st.selectbox("Multiple Lines", ["No", "No phone service", "Yes"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["No", "No internet service", "Yes"])
    online_backup = st.selectbox("Online Backup", ["No", "No internet service", "Yes"])

with col2:
    device_protection = st.selectbox("Device Protection", ["No", "No internet service", "Yes"])     
    tech_support = st.selectbox("Tech Support", ["No", "No internet service", "Yes"])
    streaming_tv = st.selectbox("Streaming TV", ["No", "No internet service", "Yes"]) 
    streaming_movies = st.selectbox("Streaming Movies", ["No", "No internet service", "Yes"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
    payment_method = st.selectbox("Payment Method", [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check", 
        "Mailed check",])
    monthly_charges = st.slider("Monthly Charges ($)", 0.0, 120.0, 65.0)
    total_charges = st.slider("Total Charges ($)", 0.0, 8000.0, 1000.0)

st.markdown("---")

# Encode inputs
def encode_input(value, options):
    return options.index(value)

if st.button("Predict Churn", type="primary"):
    input_data = pd.DataFrame([[
        encode_input(gender, ["Female", "Male"]),
        1 if senior == "Yes" else 0,
        encode_input(partner, ["No", "Yes"]),
        encode_input(dependents, ["No", "Yes"]),
        tenure,
        encode_input(phone_service, ["No", "Yes"]),
        encode_input(mulitple_lines, ["No", "No phone service", "Yes"]),
        encode_input(internet_service, ["DSL", "Fiber optic", "No"]),
        encode_input(online_security, ["No", "No internet service", "Yes"]),
        encode_input(online_backup, ["No", "No internet service", "Yes"]),
        encode_input(device_protection, ["No", "No internet service", "Yes"]),
        encode_input(tech_support, ["No", "No internet service", "Yes"]),
        encode_input(streaming_tv, ["No", "No internet service", "Yes"]),
        encode_input(streaming_movies, ["No", "No internet service", "Yes"]),
        encode_input(contract, ["Month-to-month", "One year", "Two year"]),
        encode_input(paperless_billing, ["No", "Yes"]),
        encode_input(payment_method, [
            "Bank transfer (automatic)",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"]), 
            monthly_charges,
            total_charges
        ]], columns=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
                     'PhoneService', 'MultipleLines', 'InternetService',
                     'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                     'TechSupport', 'StreamingTV', 'StreamingMovies',
                     'Contract', 'PaperlessBilling', 'PaymentMethod',
                     'MonthlyCharges', 'TotalCharges'])
    
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High Churn Risk — {probability:.1%} probability of churning")
    else:
        st.success(f"✅ Low Churn Risk — {probability:.1%} probability of churning")
                                      
        
        