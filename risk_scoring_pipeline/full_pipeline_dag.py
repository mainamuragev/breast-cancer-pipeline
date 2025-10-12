from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
import os
import logging

def ingest_diagnosis_data():
    os.makedirs("/opt/airflow/data", exist_ok=True)
    df = pd.DataFrame({
        "age": [45, 60, 30],
        "tumor_size": [2.3, 3.1, 1.8]
    })
    df.to_csv("/opt/airflow/data/diagnosis_data.csv", index=False)
    logging.info("Diagnosis data ingested.")

def score_risk_from_diagnosis():
    input_path = "/opt/airflow/data/diagnosis_data.csv"
    output_path = "/opt/airflow/data/scored_output.csv"

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Diagnosis data not found at {input_path}")

    df = pd.read_csv(input_path)
    df['risk_score'] = df['age'] * 0.2 + df['tumor_size'] * 0.5
    df.to_csv(output_path, index=False)
    logging.info(f"Risk scores saved to {output_path}")

dag = DAG(
    dag_id="full_pipeline_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
)

ingest_task = PythonOperator(
    task_id="ingest_diagnosis_data",
    python_callable=ingest_diagnosis_data,
    dag=dag,
)

score_task = PythonOperator(
    task_id="score_risk_from_diagnosis",
    python_callable=score_risk_from_diagnosis,
    dag=dag,
)

ingest_task >> score_task
