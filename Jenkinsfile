pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                echo "Installing dependencies..."
                bat 'pip install -r reqjuirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests..."
                bat 'pytest --junitxml=report.xml'
            }
        }

        stage('Publish Report') {
            steps {
                echo "Publishing report..."
                junit 'report.xml'
            }
        }
    }
}
