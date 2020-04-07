pipeline{
    agent any

    stages{
        stage("testEnv"){
            steps{
                sh 'echo "dev-test local install"'
                sh 'apt-get install docker-ce -y'
                sh 'docker stack deploy --compose-file docker-testing-compose.yml character_stack'
            }
        }
        stage("testingInstall"){
            steps{
                sh 'echo "install testing dependencies"'
                sh 'apt-get install python3-venv -y'
                sh 'python3 -m venv venv'
                sh 'source ./venv/bin/activate'
                sh 'pip3 install pytest'
                sh 'pip3 install coverage'
            }
        }
        stage("urlTesting"){
            steps{
                sh 
            }

        }
        stage("dbTesting"){
            steps{
                sh 
            }
        }
    }
}