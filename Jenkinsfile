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
		agent{
			docker { 
			    image 'python:3.7.3'
			}
    		}
		steps{
			script {
				sh 'pip install --user unittest-xml-reporting'
                    		sh 'python3 test_main.py'
			}
		}
        }
	
    }
}
