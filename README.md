# MFT Shield: A Framework for Anomaly Detection in Managed File Transfers

This project provides an end-to-end anomaly detection framework for Managed File Transfer (MFT) systems. Using server logs, network logs, and file transfer logs, we apply machine learning to detect potential anomalies and security breaches.

---

## 📂 Project Structure

```bash
├── mft_logs_sample.csv              # Sample MFT logs
├── server_logs_sample.csv           # Sample server logs
├── network_logs_sample.csv          # Sample network logs
├── network_logs_with_user.csv       # Enriched network logs (with user_id and latency)
├── mft_anomaly_detection.py         # Core anomaly detection pipeline
├── mft_dashboard.py                 # Streamlit dashboard
├── inject_anomalies_and_evaluate.py# Script to simulate anomalies and evaluate
├── mft_logs_with_anomalies.csv      # Output file with detected anomalies
├── requirements.txt                 # Python dependencies
├── README.md                        # Documentation

Real Time Anomaly Detection and Alert Dashboard for Enterprise Managed File Transfer Systems

1. Getting Started
git clone [https://github.com/asoni523/mft-anomaly-detection.git](https://github.com/asoni523/MFT_Shield)
cd mft-anomaly-detection

2. Set up environment
pip install -r requirements.txt

3. Run the Anomaly Detection Pipeline
python mft_anomaly_detection.py

4. Launch the Dashboard
streamlit run dashboard_app.py

5. Evaluation
python inject_anomalies_and_evaluate.py

6. Citation and License
If you use this repository, data, or model in your work, please cite:
Anil Kumar Soni, "MFT Shield: A Framework for Anomaly Detection in Managed File Transfers Using Machine Learning with Network, Server, and File Transfer Logs", GitHub, 2025.
[https://github.com/asoni523/mft-anomaly-detection](https://github.com/asoni523/MFT_Shield)
For academic citation, please reach out for full citation format or inclusion in upcoming publications.

7. Disclaimer
This is a research-focused prototype and is not a production-grade security solution. Use and adapt at your own risk.

8. Contributing
Feel free to fork and submit pull requests. If you improve detection logic, add visualization, or port this to real-time monitoring — contributions are welcome!

---

## `requirements.txt`

This file contains dependencies required for your project:

```txt
pandas==2.2.1
numpy==1.26.4
scikit-learn==1.4.2
streamlit==1.34.0
matplotlib==3.8.4
seaborn==0.13.2

To generate it automatically from your current Python environment:
pip freeze > requirements.txt


