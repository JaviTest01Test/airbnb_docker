from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.providers.papermill.operators.papermill import PapermillOperator

# Default arguments for the DAG
default_args = {
    'owner': 'root',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'run_airbnb_project',
    default_args=default_args,
    description='Run Airbnb Project Notebook using Docker',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
) as dag:

    start = DummyOperator(
        task_id='start',
    )

    set_permissions = BashOperator(
    task_id='set_permissions',
    bash_command="sudo chmod -R 777 /opt/airflow/airbnb_project",
    dag=dag,
    )

    # Create a task to run the notebook
    run_notebook = PapermillOperator(
        task_id='run_my_notebook',
        input_nb='/opt/airflow/airbnb_project/notebooks/main.ipynb',  # Path to the notebook
        output_nb='/opt/airflow/airbnb_project/notebooks/main_output.ipynb',  # Path to save the output
        kernel_name='python3',  # Specify the kernel name
        dag=dag,
    )

    end = DummyOperator(
        task_id='end',
    )

    start >> set_permissions >> run_notebook >> end