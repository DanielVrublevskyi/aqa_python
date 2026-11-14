pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    triggers {
        pollSCM('H/5 * * * *')
    }

    environment {
        CI = 'true'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install \
                        pytest \
                        playwright==1.65.2 \
                        allure-pytest \
                        faker \
                        requests \
                        python-dotenv

                    .venv/bin/python -m playwright install chromium
                '''
            }
        }

        stage('Run UI Tests') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'qauto-test-login',
                        usernameVariable: 'QAUTO_TEST_EMAIL',
                        passwordVariable: 'QAUTO_TEST_PASSWORD'
                    )
                ]) {
                    sh '''
                        rm -rf allure-results junit-results.xml

                        .venv/bin/python -m pytest \
                            lessons/lesson_28/tests/test_homework_28.py \
                            --alluredir=allure-results \
                            --junitxml=junit-results.xml
                    '''
                }
            }
        }
    }

    post {
        always {
            script {
                if (fileExists('junit-results.xml')) {
                    junit testResults: 'junit-results.xml'
                }

                if (fileExists('allure-results')) {
                    allure results: [[path: 'allure-results']]
                }
            }

            archiveArtifacts artifacts: 'allure-results/**',
                             allowEmptyArchive: true
        }
    }
}
