from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    "owner": "airflow",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

args = {
    "dag_id": "my_first_dag",
    "description": "This is my first DAG",
    "start_date": datetime.now(),
    "schedule_interval": "@daily",
    "default_args": default_args,
}

with DAG(**args) as dag:
    task1 = BashOperator(
        task_id="task1", bash_command="echo 'Hello World! This is task one'"
    )
    task2 = BashOperator(
        task_id="task2", bash_command="echo 'Hello World! This is task two'"
    )

    task3 = BashOperator(
        task_id="task3", bash_command="echo 'Hello World! This is task three'"
    )

    task1 >> [task2, task3]
