pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo "Checking out code..."
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing dependencies..."
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests..."
                bat '''
                set PYTHONPATH=%WORKSPACE%
                python -m pytest -v --junitxml=report.xml
                '''
            }
        }

        stage('Publish Report') {
            steps {
                echo "Publishing report..."
                junit 'report.xml'
            }
        }
    }

    post {
        success {
            echo "BUILD SUCCESS ✔"
        }
        failure {
            echo "BUILD FAILED ❌"
        }
    }
}
