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
                echo 'Setting up Python environment...'
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\python -m pip install pytest'
            }
        }
        stage('Test') {
            steps {
                echo 'Running automated tests...'
                bat 'venv\\Scripts\\python -m pytest -v'
            }
        }
    }

    post {
        success { echo 'Pipeline SUCCESS' }
        failure { echo 'Pipeline FAILED' }
    }
}