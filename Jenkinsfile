pipeline {
    agent any

    parameters {
        choice(name: 'ENV', choices: ['dev', 'test'], description: 'Choose environment to build')
    }

    environment {
        IMAGE_NAME = "my-flask-app"
        DEV_PORT = "5000"
        TEST_PORT = "6000"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${params.ENV}", "./docker")
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    if (params.ENV == 'dev') {
                        sh "docker run -d -p ${DEV_PORT}:80 --name ${IMAGE_NAME}-dev ${IMAGE_NAME}:dev"
                    } else if (params.ENV == 'test') {
                        sh "docker run -d -p ${TEST_PORT}:80 --name ${IMAGE_NAME}-test ${IMAGE_NAME}:test"
                    }
                }
            }
        }
    }

    post {
        always {
            sh "docker ps -a"
        }
    }
}
