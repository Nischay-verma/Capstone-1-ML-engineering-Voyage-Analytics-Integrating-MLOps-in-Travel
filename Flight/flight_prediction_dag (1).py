
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id='flight_price_prediction_pipeline',
    start_date=days_ago(1),
    schedule_interval='@daily', # Or a more complex schedule like '0 0 * * *' for daily at midnight
    catchup=False,
    tags=['mlops', 'flight_prediction'],
) as dag:

    # Task to pull the latest code from Git (or an artifact repository)
    clone_repo = BashOperator(
        task_id='clone_git_repo',
        bash_command='git clone https://github.com/Nischay-verma/Capstone-1-ML-engineering-Voyage-Analytics-Integrating-MLOps-in-Travel.git /tmp/repo'
    )

    # Task to install dependencies and preprocess data
    data_preprocessing = BashOperator(
        task_id='data_preprocessing',
        bash_command='cd /tmp/repo && pip install -r requirements.txt && python data_preprocessing.py'
    )

    # Task to train the flight price prediction model
    train_model = BashOperator(
        task_id='train_flight_model',
        bash_command='cd /tmp/repo && python flight_model_training.py'
    )

    # Task to build the Docker image for the Flask API
    build_docker_image = BashOperator(
        task_id='build_docker_image',
        bash_command='cd /tmp/repo && docker build -f Dockerfile.flight_price_api -t your-docker-registry/flight-price-predictor:latest .'
    )

    # Task to push the Docker image to a registry
    push_docker_image = BashOperator(
        task_id='push_docker_image',
        bash_command='docker push your-docker-registry/flight-price-predictor:latest'
    )

    # Task to deploy the model to Kubernetes
    deploy_to_kubernetes = BashOperator(
        task_id='deploy_to_kubernetes',
        bash_command='kubectl apply -f /tmp/repo/kubernetes_deployment.yaml'
    )

    # Define the task dependencies
    clone_repo >> data_preprocessing >> train_model >> build_docker_image >> push_docker_image >> deploy_to_kubernetes
