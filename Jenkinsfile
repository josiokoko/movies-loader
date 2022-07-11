def imageName = 'josiokoko/movies-loader'

node('movies'){
    stage('Checkout'){
        echo "checkout scm"
    }
    stage('Unit Tests'){
        sh "docker build -t ${imageName}-test -f Dockerfile.test ."
        sh "docker run --rm ${imageName}-test"
    }
}
