pipeline{
    agent any

    stages{
        stage("testEnv"){
            steps{
                sh 'echo "dev-test local install"'
                sh 'sudo apt update -y'
                sh 'sudo apt-get remove docker docker-engine docker.io'
                sh 'sudo apt install docker.io -y'
                sh 'sudo systemctl start docker'
                sh 'sudo systemctl enable docker'
                sh 'sudo systemctl status docker'
                sh 'newgrp docker'
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
                sh 'pip3 install ./tests/requirements.txt'
            }
        }
        stage("urlTesting"){
            steps{
                sh 'echo "Pinging URLs"'
                sh 'python3 -m coverage run -m pytest tests/url_testing.py'
                sh 'python3 -m coverage report'
            }

        }
        stage("dbTesting"){
            steps{
                sh 'echo "Probing MySQL Database"'
                sh 'source ./test.env'
                sh 'python3 -m coverage run -m pytest tests/db_testing.py'
                sh 'python3 -m coverage report'
            }
        }
        stage("seleniumTesting"){
            steps{
                sh 'echo "Mining the Selenium'
                // sh 'python3 -m coverage run -m pytest tests/db_testing.py'
                // sh 'python3 -m coverage report'
            }
        }
    }
}