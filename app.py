import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load("server_downtime_model.pkl")

st.set_page_config(page_title="Server Downtime Prediction", layout="centered")

st.title("🔧 Server Downtime Duration Prediction")
st.write("Predict server downtime (in minutes) based on system metrics and configurations.")

# Input fields
region = st.selectbox("Region", ["US-East", "EU-West", "Asia-Pacific", "India-Central"])
os_version = st.selectbox("Operating System", ["Windows", "Linux"])
cpu = st.slider("CPU Usage (%)", 0, 100, 65)
mem = st.slider("Memory Usage (%)", 0, 100, 70)
disk = st.number_input("Disk IOPS", 500, 10000, 3000)
latency = st.slider("Network Latency (ms)", 20, 400, 100)
temp = st.slider("Temperature (°C)", 10, 45, 30)

# Create DataFrame
input_df = pd.DataFrame({
    "Server_ID": ["SRV-999"],
    "Region": [region],
    "CPU_Usage": [cpu],
    "Memory_Usage": [mem],
    "Disk_IOPS": [disk],
    "Network_Latency_ms": [latency],
    "Temperature_C": [temp],
    "OS_Version": [os_version],
    "Incident_Date": [pd.Timestamp.now()]
})

if st.button("🔮 Predict Downtime"):
    pred = model.predict(input_df)[0]
    st.success(f"Estimated Downtime Duration: **{pred:.2f} minutes**")
