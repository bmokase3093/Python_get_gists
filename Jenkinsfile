pipeline {
  agent {
    docker {
      image 'python:3.11-slim'
    }

  }
  stages {
    stage('Clone Repository') {
      steps {
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

        stage('Install Dependencies') {
          steps {
            script {
              sh 'docker --version'
              sh 'pip install -r requirements.txt'  // If you want to install Python dependencies directly
            }

          }
        }

        stage('Run Tests') {
          steps {
            script {
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

        stage('Deploy the application') {
          when {
            branch 'main'
          }
          steps {
            sh 'docker run -d -p 8080:8080 ${IMAGE_NAME}'
          }
        }

      }
      environment {
        IMAGE_NAME = 'git-hub-gists'
      }
      post {
        always {
          sh 'docker system prune -f'
        }

      }
    }