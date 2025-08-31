pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo 'Setting up environment...'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Script') {
            steps {
                bat 'python app.py'
            }
        }
    }
}
