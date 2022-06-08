from datetime import datetime, timedelta

from airflow.decorators import dag, task

default_args = {
    "owner": "airflow",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

dag_args = {
    "dag_id": "dag_with_airflow_api",
    "description": "Try dag with Airflow API",
    "start_date": datetime.today() - timedelta(days=1),
    "schedule_interval": "@daily",
    "default_args": default_args,
}


@dag(**dag_args)
def dag_with_airflow_api_etl():
    @task()
    def greet():
        print("Hello!")

    @task(multiple_outputs=True)
    def i_tell_my_name():
        print("I am telling you my name")
        return {"name": "John", "age": 25}

    @task()
    def call_me(name: str, age: int):
        print(f"Hi... My name is {name}, and I'm {age} years old!")

    @task()
    def nice_to_meet_you(name: str, age: int):
        print(f"Nice to meet you {name}, you're {age} years old!")

    greet()
    name_age = i_tell_my_name()
    call_me(name_age["name"], name_age["age"])
    nice_to_meet_you(name_age["name"], name_age["age"])


dag_with_airflow_api = dag_with_airflow_api_etl()
