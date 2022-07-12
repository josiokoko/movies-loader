node("movies"){
  def customImage = docker.build("my-image:${env.BUILD_ID}")
   stage('Checkout'){
		
			checkout scm
	
    }
	    
   stage('Unit Tests'){
      customImage.push()
   }
}
