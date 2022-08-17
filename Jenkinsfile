pipeline {
  agent any
 
  environment {
	DOCKERHUB_CREDENTIALS=credentials('DockerHub-josiokoko')
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
                    		def imageTest= docker.build("${imageName}-test", "-f Dockerfile.test .")
				imageTest.inside{
				    sh "python test_main.py"
				}
				// sh "docker run --rm ${imageName}-test"
				sh "docker run --rm -v $(pwd)/reports:/app/reports ${imageName}-test" junit "$(pwd)/reports/*.xml"
			}
		}
        }
	
    }
}
