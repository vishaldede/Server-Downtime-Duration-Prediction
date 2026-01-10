# Load model
import joblib
import streamlit as st
import pandas as pd

model = joblib.load("server_downtime_model.pkl")

st.title("🔧 Server Downtime Duration Prediction")
st.write("Predict server downtime (in minutes) based on system metrics.")

# Input Fields
region = st.selectbox("Region", ["US-East", "EU-West", "Asia-Pacific", "India-Central"])
os_version = st.selectbox("Os Version", ["Windows", "Linux"])
cpu = st.slider("Cpu Usage", 0, 100, 65)
mem = st.slider("Memory Usage", 0, 100, 70)
disk = st.number_input("Disk Iops", 500, 10000, 3000)
latency = st.slider("Network Latency_Ms", 20, 400, 100)
temp = st.slider("Temperature C", 10, 45, 30)

# DataFrame
input_df = pd.DataFrame({
    "Region": [region],
    "Os_Version": [os_version],
    "Cpu_Usage": [cpu],
    "Memory_Usage": [mem],
    "Disk_Iops": [disk],
    "Network_Latency_Ms": [latency],
    "Temperature_C": [temp],
})

# Predict
if st.button("🔮Predict Downtime"):
    pred = model.predict(input_df)[0]

    st.success(f'Estimated Downtime Duration: {round(pred,2)}')

