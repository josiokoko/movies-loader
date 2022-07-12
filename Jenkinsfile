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
            		sh "docker run --rm ${imageName}-test"
		}
        }
	
    stage('Unit Tests'){
	def imageTest= docker.build("${imageName}-test", "-f Dockerfile.test .")
        	imageTest.inside{
			sh 'python test_main.py'
		} 
	} 
    }
}
