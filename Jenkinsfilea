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
                sh "cd ./python_flask/ && python3 unit-testing.py"
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
        stage("Code Quality Check via SonarQube") {
            steps {
                script  {
                    def scannerHome = tool "SonarQube";
                    withSonarQubeEnv("SonarQube") {
                        sh "${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=OWASP \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://192.168.1.217:9000 \
                            -Dsonar.login=c0a75d1a04d0d4eae36f8830789806ee8e43ff6d"
                    }
                }
            }
        }


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