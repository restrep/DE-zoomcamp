from airflow.decorators import dag, task 
from airflow.models import Variable
from pendulum import datetime
import requests

API = "https://bored-api.appbrewery.com/random"

@dag(
    start_date=datetime(2023,1,1),
    schedule="@daily",
    tags=["activity"],
    catchup=False, # dags are not trigger when part of the workflow fails
)
def find_activity():
    @task
    def get_activity():
        r = requests.get(API, timeout=10)
        return r.json()

    @task
    def write_activity_to_file(response):
        filepath = Variable.get("activity_file")
        with open(filepath, "w") as f:
            f.write(f"Today you will: {response["activity"]}]\r\n")
        return filepath

    @task 
    def read_activity_from_file(filepath):
        with open(filepath,"r") as f:
            print(f.read())

    response = get_activity()
    filepath = write_activity_to_file(response)
    read_activity_from_file(filepath)

find_activity()
