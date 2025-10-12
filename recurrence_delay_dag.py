from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 10, 10),
    'retries': 1,
}

with DAG(
    dag_id='recurrence_delay_simulation',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['recurrence', 'simulation'],
) as dag:

    run_simulation = BashOperator(
        task_id='run_simulation_script',
        bash_command='python3 /home/mainavm/simulate_delay.py'
    )
