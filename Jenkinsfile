pipeline {
    agent any

    environment {
        // Define all credentials 
        AWS_ACCESS_KEY_ID = credentials('aws_access_key_id')
        AWS_SECRET_ACCESS_KEY = credentials('aws_secret_access_key')
    }

    stages {
        stage('Checkout Git Repository') {
            steps {
                // Checkout the repository from GitHub
                git branch: 'main', credentialsId: 'git_credentials', url: 'https://github.com/kuldii/final_project_mlops.git'
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                script {
                    // Install dependencies
                    sh """
                    pip install -r requirements.txt
                    """
                }
            }
        }
        
        stage('Pull Dataset') {
            steps {
                script {
                    // pull data with DVC from AWS S3
                    sh """
                    aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
                    aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
                    dvc pull
                    """
                }
            }
        }
        
        stage('Data Quality Testing') {
            steps {
                script {
                    // Run data quality tests
                    sh """
                    python data_quality_tests.py
                    """
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build('final-project-mlops')
                }
            }
        }

        stage('Run Application in Docker') {
            steps {
                script {
                    // Run the Streamlit application in Docker
                    docker.image('final-project-mlops').run('-p 8501:8501')
                }
            }
        }
    }
}
