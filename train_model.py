import pandas as pd
from sklearn.ensemble import RandomForestClassifier 
from sklearn.preprocessing import LabelEncoder
import pickle
import numpy as np

# Load data
df = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Clean
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna(subset=['TotalCharges'])
df['Churn'] = (df['Churn'] == 'Yes').astype(int)
df = df.drop('customerID', axis=1)

# Force encode every column
le_dict ={}
for col in df.columns:
    if df[col].dtype == 'object':
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        le_dict[col] = le 
        df[col] = df[col].astype(int)

# Verify all numeric
print("Any object columns remaining:")
print(df.select_dtypes(include=['object']).columns.tolist())

# Train 
X = df.drop('Churn', axis=1)
y = df['Churn']

print("Data types after encoding:")
print(X.dtypes)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save 
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('encoders.pkl', 'wb') as f:
    pickle.dump(le_dict, f)

print("Model saved as model.pkl!")
print("Feature order:", X.columns.tolist())