pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Jenkins has checked out the GitHub repository from SCM.'
            }
        }
        stage('Build') {
            steps {
                bat 'python app.py'
            }
        }
        stage('Test') {
            steps {
                bat 'python -m unittest discover -s tests -v'
            }
        }
    }
}

