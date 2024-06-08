pipeline {
    agent any

    stages {
        stage('Git') {
            steps {
                git branch: 'main', credentialsId: 'git_credentials', url: 'https://github.com/kuldii/final_project_mlops.git'
            }
        }
        
        stage('Install Requirements'){
            steps {
                sh "pip install -r requirements.txt"
            }   
        }
        
        stage('Data Quality Testing'){
            steps {
                sh "python3 data_quality_tests.py"
            }   
        }
        
        stage('Run Apps'){
            steps {
                sh "python3 main.py"
            }   
        }
    }
}
