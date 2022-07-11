pipeline {
  agent any
 
  environment {
		DOCKERHUB_CREDENTIALS=credentials('josiokoko')
        imageName = 'josiokoko/movies-loader'
	}
    
    stages{
        stage('Checkout'){
            checkout scm
        }
        stage('Unit Tests'){
            sh "docker build -t ${imageName}-test -f Dockerfile.test ."
            sh "docker run --rm ${imageName}-test"
        }
    }
}
