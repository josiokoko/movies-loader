pipeline {
  agent any
 
  environment {
	DOCKERHUB_CREDENTIALS=credentials('docker-josiokoko')
        imageName = 'josiokoko/movies-loader'
    }
    
    stages {
	    
        stage('Checkout'){
		steps{
			checkout scm
		}
        }
	    
        stage('Unit Tests'){
		steps{
			script {
                    		sh 'python3 test_main.py'
			}
		}
        }
	
    }
}
