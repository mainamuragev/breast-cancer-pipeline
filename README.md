# 🧠 Risk Scoring Pipeline for Breast Cancer Diagnosis

This project ingests diagnosis data, computes risk scores, and serves results via a FastAPI backend.

## 🔗 API Endpoints

- `GET /risk-scores` → Returns scored diagnosis data
- `GET /health` → Confirms backend is live
- `POST /trigger-ingestion` → Triggers Airflow DAG

## 📦 Stack

- Airflow DAGs for ingestion and scoring
- FastAPI backend
- CSV output served as JSON

## 🛠️ Setup

```bash
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
