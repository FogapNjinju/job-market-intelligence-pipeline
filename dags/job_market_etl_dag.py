from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import subprocess
import os
from pathlib import Path

# Default arguments for the DAG
default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'job_market_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for job market intelligence',
    schedule_interval=timedelta(days=1),  # Run daily
    catchup=False,
)

def run_extract():
    """Run the extract script"""
    script_path = Path(__file__).parent.parent / 'src' / 'extract.py'
    result = subprocess.run(['python', str(script_path)], capture_output=True, text=True, cwd=script_path.parent.parent)
    if result.returncode != 0:
        raise Exception(f"Extract failed: {result.stderr}")
    print(result.stdout)

def run_transform():
    """Run the transform script"""
    script_path = Path(__file__).parent.parent / 'src' / 'transform.py'
    result = subprocess.run(['python', str(script_path)], capture_output=True, text=True, cwd=script_path.parent.parent)
    if result.returncode != 0:
        raise Exception(f"Transform failed: {result.stderr}")
    print(result.stdout)

def run_load():
    """Run the load script"""
    script_path = Path(__file__).parent.parent / 'src' / 'load.py'
    result = subprocess.run(['python', str(script_path)], capture_output=True, text=True, cwd=script_path.parent.parent)
    if result.returncode != 0:
        raise Exception(f"Load failed: {result.stderr}")
    print(result.stdout)

# Define tasks
extract_task = PythonOperator(
    task_id='extract',
    python_callable=run_extract,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=run_transform,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load',
    python_callable=run_load,
    dag=dag,
)

# Set task dependencies
extract_task >> transform_task >> load_task