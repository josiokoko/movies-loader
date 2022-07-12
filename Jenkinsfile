pipeline {
  agent {
	  dockerfile true
	}
 
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
            		sh "docker run --rm ${imageName}-test"
		}
        }
	    
    }
}
