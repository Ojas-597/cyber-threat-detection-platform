# 🛡️ AI-Powered Cyber Threat Detection Platform

An enterprise-grade AI-driven Cybersecurity Threat Detection and Incident Response Platform developed as an MSc Computer Science (Cybersecurity) research project.

This platform integrates:
- Artificial Intelligence
- Threat Intelligence
- Blockchain-based Integrity
- SIEM Concepts
- MITRE ATT&CK Framework
- CVE Intelligence
- Intrusion Detection
- Malware Detection
- Phishing Detection
- Real-Time Threat Monitoring

---

# 📌 Project Objectives

The goal of this research project is to design and implement a scalable cybersecurity framework capable of:

- Detecting cyber threats in real time
- Monitoring suspicious network activity
- Integrating threat intelligence feeds
- Performing AI-based attack classification
- Mapping threats to MITRE ATT&CK techniques
- Maintaining tamper-proof blockchain logs
- Providing automated incident response mechanisms
- Visualizing threats using interactive dashboards

---

# 🚀 Features

## 🔐 Authentication & Security
- JWT Authentication
- Multi-Factor Authentication (MFA)
- Role-Based Access Control (RBAC)

## 🧠 AI Threat Detection
- Intrusion Detection System (IDS)
- Malware Detection
- Phishing URL Detection
- Threat Classification Engine

## 🌐 Threat Intelligence
- VirusTotal Integration
- CVE Feed Monitoring
- MITRE ATT&CK Mapping

## ⛓️ Blockchain Security
- Blockchain Log Integrity
- SHA256 Hash Verification
- Tamper Detection

## 📊 Dashboard & Analytics
- Real-Time Threat Dashboard
- Attack Visualization Graphs
- Threat Severity Analytics
- Incident Monitoring

## ⚙️ DevOps & Deployment
- Docker Support
- Kubernetes Deployment
- GitHub Actions CI/CD
- ELK Stack Integration

---

# 🏗️ Project Architecture

```text
Frontend (React Dashboard)
        ↓
FastAPI Backend APIs
        ↓
Threat Detection Engine
        ↓
Machine Learning Models
        ↓
MongoDB + Elasticsearch
        ↓
Threat Intelligence Layer
        ↓
Blockchain Integrity Logs
```

---

# 📂 Project Structure

```text
cyber-threat-detection-platform/
│
├── backend/
│   ├── api/
│   ├── authentication/
│   ├── intrusion_detection/
│   ├── phishing_detection/
│   ├── malware_detection/
│   ├── blockchain_logs/
│   ├── incident_response/
│   ├── threat_intelligence/
│   ├── database/
│   └── app.py
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   ├── charts/
│   └── App.js
│
├── machine_learning/
│   ├── models/
│   ├── preprocessing/
│   ├── training/
│   └── evaluation/
│
├── blockchain/
├── deployment/
├── docs/
└── README.md
```

---

# 🛠️ Technology Stack

## Backend
- FastAPI
- Python
- JWT Authentication
- Scapy
- Pydantic

## Frontend
- React.js
- Recharts
- Axios
- Framer Motion

## Database
- MongoDB
- Elasticsearch

## Machine Learning
- Scikit-learn
- TensorFlow
- Pandas
- NumPy

## DevOps
- Docker
- Kubernetes
- GitHub Actions

---

# 📊 Modules Implemented

| Module | Status |
|---|---|
| Authentication System | ✅ |
| Threat Management APIs | ✅ |
| Intrusion Detection | ✅ |
| Phishing Detection | ✅ |
| Malware Scanner | ✅ |
| Blockchain Logs | ✅ |
| CVE Feed Fetcher | ✅ |
| VirusTotal Integration | ✅ |
| MITRE ATT&CK Mapping | ✅ |
| AI Chatbot Assistant | ✅ |
| React Dashboard | ✅ |

---

# 🔥 API Endpoints

## Threat APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | `/threats/` | Get all threats |
| GET | `/threats/live` | Get live threats |
| POST | `/threats/add` | Add new threat |
| PUT | `/threats/update/{id}` | Update threat |
| DELETE | `/threats/delete/{id}` | Delete threat |

---

# ⚡ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/cyber-threat-detection-platform.git
```

---

## 2️⃣ Backend Setup

```bash
cd backend

pip install -r requirements.txt

uvicorn app:app --reload
```

Backend Runs At:

```text
http://127.0.0.1:8000
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

## 3️⃣ Frontend Setup

```bash
cd frontend

npm install

npm start
```

Frontend Runs At:

```text
http://localhost:3000
```

---

# 🧪 Example Threat JSON

```json
{
  "type": "Ransomware",
  "severity": "Critical",
  "source_ip": "45.22.11.5",
  "destination_ip": "10.0.0.7",
  "protocol": "SMB",
  "status": "Active",
  "mitre_attack_id": "T1486",
  "confidence_score": 97.8
}
```

---

# 📈 Research Contributions

This research project contributes to:
- AI-driven cyber threat analysis
- Real-time incident response systems
- Blockchain-integrated forensic logging
- Threat intelligence automation
- SIEM-inspired cybersecurity frameworks

---

# 📚 Future Enhancements

- Real-time WebSocket Monitoring
- AI-based Anomaly Detection
- Zero Trust Architecture
- Dark Web Threat Intelligence
- Cloud-native SOC Deployment
- Automated Threat Hunting

---

# 🧑‍💻 Author

## Ojaswita Ranjit Desai
## MSc Computer Science (Cybersecurity)

Research Project:
**AI-Powered Cyber Threat Detection Platform**

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Acknowledgements

- MITRE ATT&CK Framework
- NIST NVD CVE Database
- VirusTotal API
- FastAPI
- React.js
- MongoDB
- Elasticsearch
