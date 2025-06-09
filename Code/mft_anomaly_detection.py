# mft_anomaly_detection.py - Load/Normalize/Train Model
# Created By: Anil Soni
# Created: May 05, 2025
# Updated: June 05, 2025

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Load the datasets
mft = pd.read_csv('mft_logs_sample.csv')
network = pd.read_csv('network_logs_with_user.csv')
server = pd.read_csv('server_logs_sample.csv')

# Merge the datasets on timestamp and user_id (simplified join for demo purposes)
df = mft.merge(network, on=['timestamp', 'user_id'], how='left')
df = df.merge(server, on=['timestamp', 'user_id'], how='left')

# Fill missing values and normalize
df.fillna(0, inplace=True)
features = ['file_size_MB', 'transfer_time_sec', 'failed_logins', 'cpu_usage_percent', 'memory_usage_percent', 'network_latency']
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[features])
df_scaled = pd.DataFrame(df_scaled, columns=features)

# Train Isolation Forest model
model = IsolationForest(n_estimators=100, contamination=0.12, random_state=42)
model.fit(df_scaled)
df['anomaly_score'] = model.decision_function(df_scaled)
df['anomaly'] = model.predict(df_scaled)
df['anomaly'] = df['anomaly'].map({1: 0, -1: 1})  # 1 for anomaly

# Save to CSV
df.to_csv('mft_logs_with_anomalies.csv', index=False)
