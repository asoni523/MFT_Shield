# network_logs_with_user.py - enhance network log
# Created By: Anil Soni
# Created: June 1, 2025
# Updated: 

import pandas as pd

# Load the logs
mft_logs = pd.read_csv("mft_logs_sample.csv")
network_logs = pd.read_csv("network_logs_sample.csv")

# Convert timestamps to datetime
mft_logs['timestamp'] = pd.to_datetime(mft_logs['timestamp'])
network_logs['timestamp'] = pd.to_datetime(network_logs['timestamp'])

# Round timestamps to nearest minute
mft_logs['timestamp_min'] = mft_logs['timestamp'].dt.floor('min')
network_logs['timestamp_min'] = network_logs['timestamp'].dt.floor('min')

# Merge to associate user_id based on rounded timestamp
network_logs_with_user = pd.merge(
    network_logs,
    mft_logs[['timestamp_min', 'user_id']],
    on='timestamp_min',
    how='left'
)

# Fill missing user_ids (optional: drop or forward-fill based on your use case)
network_logs_with_user['user_id'] = network_logs_with_user['user_id'].fillna('unknown')

# Calculate network_latency (example formula)
network_logs_with_user['network_latency'] = (
    network_logs_with_user['bytes_sent'] + network_logs_with_user['bytes_received']
) / 1000.0  # assuming KB-scale for latency proxy

# Save for downstream use
network_logs_with_user.to_csv("network_logs_with_user.csv", index=False)

print("✅ Done. Output saved as 'network_logs_with_user.csv'")

