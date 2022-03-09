pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh "rm -rf mpwa"
                sh "git clone https://github.com/analouro/mpwa.git"
                //
            }
        }
        stage('Install Docker and Docker compose') {
            steps {
                sh 'sudo apt-get update'
                sh 'sudo apt update'
                sh 'mkdir -p ~/.docker/cli-plugins/'
                sh 'curl -SL "https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-linux-x86_64" -o ~/.docker/cli-plugins/docker-compose'
                sh 'chmod +x ~/.docker/cli-plugins/docker-compose'
                //
            }
        }
        stage('Deploy') {
            steps {
                "sudo docker-compose pull && sudo -E DB_PASSWORD=${DB_PASSWORD} docker-compose up -d"
                //
            }
        }
    }
}