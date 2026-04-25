pipeline {
    agent any

    stages {

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
        echo ===== WORKSPACE CHECK =====
        cd
        dir

        echo ===== SETTING PYTHON PATH =====
        set PYTHONPATH=%WORKSPACE%

        echo ===== RUNNING TESTS =====
        python -m pytest -v --junitxml=report.xml
        '''
    }
}
