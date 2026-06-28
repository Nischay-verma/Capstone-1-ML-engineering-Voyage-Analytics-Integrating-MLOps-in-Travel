from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="flight_price_prediction_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["mlops", "flight_prediction"],
) as dag:

    # Task to pull the latest code from GitHub
    clone_repo = BashOperator(
        task_id="clone_git_repo",
        bash_command="git clone https://github.com/Nischay-verma/Capstone-1-ML-engineering-Voyage-Analytics-Integrating-MLOps-in-Travel.git /tmp/repo"
    )

    # Install dependencies and preprocess data
    data_preprocessing = BashOperator(
        task_id="data_preprocessing",
        bash_command="cd /tmp/repo && pip install -r requirements.txt && python data_preprocessing.py"
    )

    # Train the model
    train_model = BashOperator(
        task_id="train_flight_model",
        bash_command="cd /tmp/repo && python flight_model_training.py"
    )

    # Build Docker image
    build_docker_image = BashOperator(
        task_id="build_docker_image",
        bash_command="cd /tmp/repo && docker build -f Dockerfile.flight_price_api -t your-docker-registry/flight-price-predictor:latest ."
    )

    # Push Docker image
    push_docker_image = BashOperator(
        task_id="push_docker_image",
        bash_command="docker push your-docker-registry/flight-price-predictor:latest"
    )

    # Deploy to Kubernetes
    deploy_to_kubernetes = BashOperator(
        task_id="deploy_to_kubernetes",
        bash_command="kubectl apply -f /tmp/repo/kubernetes_deployment.yaml"
    )

    # Task dependencies
    (
        clone_repo
        >> data_preprocessing
        >> train_model
        >> build_docker_image
        >> push_docker_image
        >> deploy_to_kubernetes
    )
