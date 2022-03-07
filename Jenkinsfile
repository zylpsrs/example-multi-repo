pipeline {
  agent {
    kubernetes {
      defaultContainer 'jnlp'
    }
  }

  stages {
    stage('test') {
      steps {
        script {
          echo 'hello world!'
        }
      }
    }
  }
}
