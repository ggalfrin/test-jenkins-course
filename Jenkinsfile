pipeline {
    // agent { docker { image 'python_with_pytest:latest' } }
    //agent any
    agent { docker { image 'python_with_pytest:latest' } }
    stages {
        stage('test') {
            steps {
                //sh 'PYTHONPATH=. pytest'
                sh 'python -m pytest tests'
            }
        }
    }
}
