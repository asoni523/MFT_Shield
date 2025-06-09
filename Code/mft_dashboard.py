
# mft_dashboard.py - create Streamlit dashboards
# Created By: Anil Soni
# Created: May 08, 2025
# Updated: June 04, 2025

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📊 MFT Anomaly Detection Dashboard")

# Load data
data = pd.read_csv("mft_logs_with_anomalies.csv")

# Sidebar filters
st.sidebar.header("Filter Data")
anomaly_filter = st.sidebar.selectbox("Filter by Anomaly", ["All", "Normal (0)", "Anomaly (1)"])
if anomaly_filter == "Normal (0)":
    data = data[data["anomaly"] == 0]
elif anomaly_filter == "Anomaly (1)":
    data = data[data["anomaly"] == 1]

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(data))
col2.metric("Anomalies", len(data[data["anomaly"] == 1]))
col3.metric("Normal", len(data[data["anomaly"] == 0]))

# Anomaly Score Distribution
st.subheader("📉 Anomaly Score Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(data['anomaly_score'], bins=30, kde=True, ax=ax1)
st.pyplot(fig1)

# Scatter: File Size vs Transfer Time
st.subheader("📌 File Size vs Transfer Time")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=data, x='file_size_MB', y='transfer_time_sec', hue='anomaly', palette='Set1', ax=ax2)
st.pyplot(fig2)

# Top Users with Anomalies
st.subheader("👤 Top Users with Anomalies")
top_users = data[data["anomaly"] == 1]["user_id"].value_counts().head(10)
st.bar_chart(top_users)
