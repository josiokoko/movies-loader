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
			sh "python --version"
			sh "docker build -t ${imageName}-test -f Dockerfile.test ."
			sh "docker run --rm -v $PWD/report:/app/report ${imageName}-test"
        		junit "$PWD/report/*.xml"
		}
        }
	
    }
}
