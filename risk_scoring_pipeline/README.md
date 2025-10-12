<<<<<<< HEAD
# 🩺 Breast Cancer Diagnostic Ingestion Pipeline

This pipeline ingests structured diagnostic data into PostgreSQL for downstream analysis and recurrence prediction. Built for reproducibility, clarity, and public health impact.

## 🚀 Usage

1. Install dependencies:
```bash
pip install pandas psycopg2-binary
=======

#  Breast Cancer Recurrence Ingestion Pipeline

This Airflow-powered pipeline ingests breast cancer recurrence data with simulated delay logic to reflect real-world latency. It’s designed for reproducibility, modular orchestration, and public portfolio deployment — part of a broader health impact initiative.

---

##  Project Goals

- Ingest recurrence data for breast cancer analysis
- Simulate ingestion delays for reproducibility and testing
- Log delay and ingestion metadata for validation
- Scaffold downstream validation and analytics
- Prepare for public release and global outreach

---

## ⚙ DAG Overview

**DAG ID**: `recurrence_ingestion_dag`  
**Schedule**: Manual trigger (`schedule_interval=None`)  
**Tags**: `breast_cancer`, `ingestion`

### 🔧 Tasks

1. `simulate_delay`  
   - Introduces a randomized delay (5–15 seconds)  
   - Logs timestamp and delay duration to `delay_log.txt`

2. `run_ingestion_script`  
   - Executes ingestion logic via BashOperator  
   - Runs `ingest_recurrence.py` to pull and process recurrence data

---

##  File Structure

```
airflow/
├── dags/
│   ├── recurrence_dag.py
│   └── ingestion/
│       └── ingest_recurrence.py
├── delay_log.txt
├── README.md
=======
# Breast Cancer Diagnostic Pipeline

A modular data ingestion pipeline for breast cancer diagnostic data using Python and PostgreSQL. Built for reproducibility, clarity, and real-world health impact.

---

##  Features

- Ingests diagnostic features into PostgreSQL
- Cleans column names and aligns schema
- Uses environment variables for secure config
- Handles recurrence fallback for missing labels
- Ready for Airflow orchestration and dashboarding

---

##  Setup Instructions

```bash
git clone https://github.com/mainamuragev/breast-cancer-pipeline.git
cd breast_cancer_pipeline
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
>>>>>>> dd0c057865880bdfe18abf1e4276edff10db3cee
```


## Delay Logging

Each DAG run appends a timestamped entry to:

```
~/airflow/delay_log.txt
```

Example:
```
2025-10-11T11:15:31.652832 | Delay: 11 seconds
```

This log supports reproducibility and downstream validation.

##  Next Steps

- Patch ingestion script to log metadata (start/end time, row count, output path)
- Scaffold a validation DAG to read and verify delay + ingestion logs
- Add screenshots of DAG UI, Gantt view, and logs
- Document environment setup for reproducibility

---

##  Author

**Maina Murage**  
Mechanical Engineering → Data Engineering  
Focused on reproducible pipelines for health impact  
📧 muragevincent39@gmail.com  
🌍 Nairobi, Kenya


##  Environment Configuration

Create a `.env` file based on this template:

```env
DB_USER=your_username
DB_PASS=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
```

---

##  Recurrence Ingestion Pipeline

Located in `ingest_recurrence.py`, this script ingests diagnostic data into PostgreSQL with:

- Fallback recurrence labels (`'unknown'` if missing)
- Manual schema alignment for headerless CSVs
- Row-level validation and debug visibility

### Run the ingestion:

```bash
python ingest_recurrence.py
```

### Validate in SQL:

```sql
SELECT recurrence, COUNT(*) FROM diagnostics GROUP BY recurrence;
```

---

## Data Source

- [UCI Breast Cancer Diagnostic Dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))

---

##  Future Extensions

- Airflow DAG orchestration
- Grafana or Streamlit dashboard
- ML prediction pipeline
- Interactive self-check tools

---

##  Built in Nairobi

Crafted by [Maina Murage](https://github.com/mainamuragev) for public health awareness and global reproducibility.
>>>>>>> dd0c057865880bdfe18abf1e4276edff10db3cee

>>>>>>> 6aefc4cb6dfffa65bd27ccf1f339faa470df8784
