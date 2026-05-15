from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="ecommerce_sales_pipeline",
    default_args=default_args,
    schedule=None,
    catchup=False,
    tags=["ecommerce", "etl"],
) as dag:

    ingest = BashOperator(
        task_id="ingest_data",
        bash_command="python /opt/airflow/scripts/ingest.py",
    )

    clean = BashOperator(
        task_id="clean_data",
        bash_command="python /opt/airflow/scripts/clean.py",
    )

    transform = BashOperator(
        task_id="transform_data",
        bash_command="python /opt/airflow/scripts/transform.py",
    )

    load = BashOperator(
        task_id="load_to_postgres",
        bash_command="python /opt/airflow/scripts/load.py",
    )

    ingest >> clean >> transform >> load