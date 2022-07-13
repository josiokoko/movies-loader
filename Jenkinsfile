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
				def imageTest = docker.build("${imageName}-test", "-f Dockerfile.test .")
				sh "pip install unittest-xml-reporting"
				sh "python test_main.py"
				sh "docker run --rm -v $PWD/reports:/app/reports ${imageName}-test"
				junit "$PWD/reports/*.xml"
			}
		}
        }
	
    }
}
