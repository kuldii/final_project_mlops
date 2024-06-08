pipeline {
    agent any

    environment {
        // Define the virtual environment directory
        VENV = 'venv'
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
                    // Create a virtual environment and install dependencies
                    sh """
                    python3 -m venv ${VENV}
                    source ${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    """
                }
            }
        }

        stage('Pull Dataset') {
            steps {
                script {
                    // Use the virtual environment to run DVC
                    sh """
                    source ${VENV}/bin/activate
                    dvc pull
                    """
                }
            }
        }
        
        stage('Data Quality Testing') {
            steps {
                script {
                    // Run data quality tests within the virtual environment
                    sh """
                    source ${VENV}/bin/activate
                    python data_quality_tests.py
                    """
                }
            }
        }
        
        stage('Run Application') {
            steps {
                script {
                    // Run the Streamlit application within the virtual environment
                    sh """
                    source ${VENV}/bin/activate
                    streamlit run main.py
                    """
                }
            }
        }
    }
    
    post {
        always {
            // Clean up the virtual environment after the pipeline finishes
            sh "rm -rf ${VENV}"
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
