from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

dag_args = {
    "dag_id": "dag_with_python_operator",
    "description": "Try dag with Python Operator",
    "start_date": datetime.today() - timedelta(days=1),
    "schedule_interval": "@daily",
    "default_args": default_args,
}


def greet():
    print("Hello!")


def i_tell_my_name(ti):
    ti.xcom_push(key="name", value="John")
    ti.xcom_push(key="age", value=25)
    print("I am telling you my name ang age")


def call_me(ti):
    name = ti.xcom_pull(task_ids="i_tell_my_name", key="name")
    age = ti.xcom_pull(task_ids="i_tell_my_name", key="age")
    print(f"Hi... My name is {name}, and I'm {age} years old!")


def nice_to_meet_you(ti):
    name = ti.xcom_pull(task_ids="i_tell_my_name", key="name")
    age = ti.xcom_pull(task_ids="i_tell_my_name", key="age")
    print(f"Nice to meet you {name}, you're {age} years old!")


with DAG(**dag_args) as dag:
    task1 = PythonOperator(task_id="greet", python_callable=greet)

    task2 = PythonOperator(task_id="i_tell_my_name", python_callable=i_tell_my_name)

    task3 = PythonOperator(
        task_id="call_me",
        python_callable=call_me,
    )

    task4 = PythonOperator(task_id="nice_to_meet_you", python_callable=nice_to_meet_you)

    task1 >> task2 >> [task3, task4]
