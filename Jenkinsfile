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
				imageTest.inside{
					sh "python test_main.py"
				}
				sh "docker run --rm -u jenkins -v $PWD/reports:/app/report ${imageName}-test"
				junit "$PWD/reports/*.xml"
			}
		}
        }
	
    }
}
