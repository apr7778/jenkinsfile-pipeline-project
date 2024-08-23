pipeline {
    agent any
    stages {
        stage('run') {
            steps {
                echo 'Clarusway_Way to Reinvent Yourself'
                sh 'python3 --version'i
                whoami
                sh 'python3 pipeline.py'
            }
        }
    }
}
