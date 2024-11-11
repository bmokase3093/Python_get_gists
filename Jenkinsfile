pipeline {
    agent {
        docker { image 'python:3.11-slim' }
    }

    environment {
        IMAGE_NAME = "git-hub-gists"
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Use credentials for private repo access
                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/bmokase3093/Python_get_gists.git',
                        credentialsId: 'GitHub'
                    ]]
                ])
            }
        }
        
        // Stage for installing dependencies
        stage('Install Dependencies') {
            steps {
                script {
                    // Ensure Docker is installed on the Jenkins agent
                    sh 'docker --version'
                    sh 'pip install -r requirements.txt'  // If you want to install Python dependencies directly
                }
            }
        }

        // Stage for running tests
        stage('Run Tests') {
            steps {
                script {
                    // Run the tests within the Docker container
                    sh 'docker build -t ${IMAGE_NAME} .'
                    sh 'docker run --rm ${IMAGE_NAME} pytest test_app.py' // Run pytest in the container
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                sh 'docker run -d -p 8080:8080 ${IMAGE_NAME}'
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f'
        }
    }
}