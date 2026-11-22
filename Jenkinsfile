pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Code fetched from GitHub'
            }
        }
        stage('Build') {
            steps {
                echo 'Checking Python...'
                sh 'python3 --version'
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install pytest'
            }
        }
        stage('Test') {
            steps {
                echo 'Running automated tests...'
                sh './venv/bin/python -m pytest -v'
            }
        }
    }

    post {
        success { echo 'Pipeline SUCCESS' }
        failure { echo 'Pipeline FAILED' }
    }
}