def imageName = 'josiokoko/movies-loader'

node('movies'){
    stage('Checkout'){
        checkout scm
    }
    stage('Unit Tests'){
        sh "docker:dind build -t ${imageName}-test -f Dockerfile.test ."
        sh "docker:dind run --rm ${imageName}-test"
    }
}
