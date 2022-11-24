pipeline {
    agent any
    stages {
        stage('Check environment') {
            steps {
                python3 --version
            }
        }
        stage('Clone Git') {
            steps {
                git 'https://github.com/harsha-deep/Jenkins-Demo.git'
            }
        }
        stage('Build Code') {
            steps {
                sh 'chmod u+x main.py'
                sh './main.py'
            }
        }
        stage('Test Code') {
            steps {
                sh 'chmod u+x test.py'
                sh './test.py'
            }
        }
    }
}
