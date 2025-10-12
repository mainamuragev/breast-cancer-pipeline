from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

def ingest_data():
    df = pd.read_csv('/opt/airflow/data/diagnosis_input.csv')
    df.to_csv('/opt/airflow/data/intermediate.csv', index=False)

def score_risk():
    df = pd.read_csv('/opt/airflow/data/intermediate.csv')
    df['risk_score'] = df['age'] * 0.1 + df['tumor_size'] * 3
    df.to_csv('/opt/airflow/data/scored_output.csv', index=False)

def summarize():
    df = pd.read_csv('/opt/airflow/data/scored_output.csv')
    print(f"Total: {len(df)} | Mean Risk: {df['risk_score'].mean():.2f} | Age Range: {df['age'].min()}–{df['age'].max()}")

with DAG(
    dag_id='diagnosis_risk_pipeline',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=['diagnosis', 'risk'],
) as dag:

    t1 = PythonOperator(task_id='ingest_diagnosis_data', python_callable=ingest_data)
    t2 = PythonOperator(task_id='score_risk_from_diagnosis', python_callable=score_risk)
    t3 = PythonOperator(task_id='summarize_output', python_callable=summarize)

    t1 >> t2 >> t3
