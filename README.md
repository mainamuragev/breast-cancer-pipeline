
# 🩺 Diagnosis Risk Pipeline

Part of the **Breast Cancer Analytics Suite**, this Apache Airflow DAG ingests diagnosis data, applies a custom risk scoring model, and logs summary statistics for downstream analytics and public health impact.

---

## 📦 Pipeline Overview

This DAG orchestrates three core tasks:

| Task ID                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `ingest_diagnosis_data`  | Loads diagnosis entries from a CSV source                                  |
| `score_risk_from_diagnosis` | Applies a risk scoring algorithm based on age and tumor size             |
| `summarize_output`       | Logs total entries, mean risk score, and age range from the scored output   |

---

## 📁 Input Format

The pipeline expects a CSV file at:

```
/opt/airflow/data/diagnosis_input.csv
```

With the following schema:

```csv
age,tumor_size
60,3.1
30,1.8
```

---

## 📤 Output

Scored results are written to:

```
/opt/airflow/data/scored_output.csv
```

Sample output:

```csv
age,tumor_size,risk_score
60,3.1,13.55
30,1.8,6.9
```

---

## 🚀 How to Run

Trigger manually via Airflow UI or CLI:

```bash
airflow dags trigger diagnosis_risk_pipeline
```

Monitor task logs in the UI or via:

```bash
airflow tasks run diagnosis_risk_pipeline summarize_output <execution_date>
```

Replace `<execution_date>` with the actual timestamp of the DAG run.

---

## 🧠 Summary Stats

After execution, the DAG logs:

- ✅ Total entries processed
- 📊 Mean risk score
- 👥 Age range of patients

---

## 🛠 Deployment Notes

- Airflow version: *confirm your version here*
- DAG location: `~/airflow/dags/diagnosis_risk_pipeline.py`
- Python version: *confirm your version here*
- Dependencies: `pandas`, `apache-airflow`

---

## 🌍 Impact & Next Steps

This pipeline lays the foundation for full-spectrum breast cancer analytics. Future extensions may include:

- Genetic marker ingestion
- Recurrence risk scoring
- Visualization dashboards
- Public API endpoints
