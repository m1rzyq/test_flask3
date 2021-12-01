pipeline {
   agent any
   stages {
        //stage('PreBuild') {
            //agent any
            //steps {
                //
                //sh 'curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
                //sh 'chmod +x /usr/local/bin/docker-compose'
                //sh 'docker compose --version'
            //}
        //}
        stage('test') {
            agent any
            steps {
                sh "sudo docker-compose up --build -d"
            }
        }
        stage('unit-test') {
            agent any
            steps {
                sh "python3 /python_flask/unittest.py"
            }
        }
        //agent {
            
            //docker {
              //  image 'python:3.9.7-alpine3.13'
        
        //steps {
               // sh 'sudo docker-compose up'
                // sh 'python test.py'
           // }
        //}
        stage ("OWASP Dependency Check") {
            steps{
                dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'owasp'
            }
        }
   }
  post{
     success{
        dependencyCheckPublisher pattern: 'dependency-check-report.xml'
     }
  }
}