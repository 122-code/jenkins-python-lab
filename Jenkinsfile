pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo "📥 Checking out code from GitHub..."
                git branch: 'main', url: 'https://github.com/YOUR-USERNAME/jenkins-python-lab.git'
            }
        }

        stage('Setup Environment') {
            steps {
                echo "📦 Installing Python dependencies..."
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "🧪 Running pytest..."
                bat 'pytest --junitxml=report.xml'
            }
        }

        stage('Publish Test Report') {
            steps {
                echo "📊 Publishing test results..."
                junit 'report.xml'
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline executed successfully!"
        }

        failure {
            echo "❌ Pipeline failed. Check logs!"
        }

        always {
            echo "🧹 Cleaning workspace..."
        }
    }
}