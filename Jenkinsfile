pipeline {
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/harsha-deep/Jenkins-Demo.git'
            }
        }
        stage('Code Build add') {
            steps {
                sh 'chmod u+x adder.py'
                sh './adder.py'
            }
        }
        stage('Code Build mult') {
            steps {
                sh 'chmod u+x mult.py'
                sh './mult.py'
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
