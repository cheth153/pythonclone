pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Cloning the Git repository...'
                git url: 'https://github.com/cheth153/pythonclone.git', branch: 'main'
            }
        }

        stage('Validate & Test') {
            steps {
                echo 'Installing dependencies'
                bat 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pip.exe install -r requirements.txt'

                echo 'Running tests'
                dir("${WORKSPACE}") {
                    bat 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pytest'
                }
            }
        }

        stage('Prepare Dockerfile') {
            steps {
                echo ' Creating Dockerfile'
                   bat '''
                   echo FROM python:3.9-slim
                   echo WORKDIR /app
                   echo COPY requirements.txt .
                   echo RUN pip install --no-cache-dir -r requirements.txt
                   echo COPY . .
                   echo EXPOSE 5000
                   echo CMD ["python", "app.py"]
                '''

                    
        
                echo 'Dockerfile created successfully'
            }
        }
    }

}
