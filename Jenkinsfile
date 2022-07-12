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
			sh "docker build -t ${imageName}-test -f Dockerfile.test ."
			sh "docker run --rm -v $PWD/reports:/app/reports ${imageName}-test"
        		junit "$PWD/reports/*.xml"
		}
        }
	

    }
}
