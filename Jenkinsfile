
pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install pytest playwright allure-pytest faker
                '''
            }
        }
    }
}
