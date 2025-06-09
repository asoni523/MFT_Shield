# compute_confusion_matrix.py - confusion matrix for model performance evaluation
# Created By: Anil Soni
# Created: June 01, 2025
# Updated: June 08, 2025

import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Load your CSV
df = pd.read_csv("mft_logs_with_true_labels.csv")

# Ensure correct data types
df['actual_anomaly'] = df['actual_anomaly'].astype(int)
df['anomaly'] = df['anomaly'].astype(int)

# Generate confusion matrix and classification report
cm = confusion_matrix(df['actual_anomaly'], df['anomaly'])
report = classification_report(df['actual_anomaly'], df['anomaly'], target_names=['Normal', 'Anomaly'])

print("Confusion Matrix:\n", cm)
print("\nClassification Report:\n", report)

# Plot confusion matrix
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=["Pred Normal", "Pred Anomaly"], yticklabels=["Actual Normal", "Actual Anomaly"])
plt.title("Confusion Matrix")
plt.ylabel("True Label")
plt.xlabel("Predicted Label")
plt.show()
