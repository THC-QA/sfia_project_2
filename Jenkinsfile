pipeline{
    agent any

    stages{
        stage("testEnv"){
            steps{
                sh 'echo "dev-test local install"'
                sh 'sudo apt update -y'
                // sh 'sudo apt-get remove docker docker-engine docker.io -y'
                sh 'sudo apt install docker.io -y'
                sh 'sudo apt install docker-compose -y'
                sh 'sudo systemctl start docker'
                sh 'sudo systemctl enable docker'
                sh 'sudo systemctl status docker'
                sh 'sudo usermod -aG docker $USER'
            }
        }
        stage("testingInstall"){
            steps{
                sh 'echo "install testing dependencies"'
                sh 'sudo apt install python3-venv -y'
                sh 'python3 -m venv venv'
                sh '. /var/lib/jenkins/workspace/sfia_project_2/venv/bin/activate'
                sh 'pip3 install pytest'
                sh 'pip3 install coverage'
                sh 'pip3 install -r /var/lib/jenkins/workspace/sfia_project_2/requirements.txt'
                // sh 'docker swarm leave -f'
                sh 'docker swarm init'
                sh 'docker stack deploy --compose-file /var/lib/jenkins/workspace/sfia_project_2/docker-testing-compose.yml test_character_stack'
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
                sh '. ./test.env'
                sh 'python3 -m coverage run -m pytest tests/db_testing.py'
                sh 'python3 -m coverage report'
            }
        }
        stage("seleniumTesting"){
            steps{
                sh 'echo "Mining the Selenium'
                // sh 'python3 -m coverage run -m pytest tests/db_testing.py'
                // sh 'python3 -m coverage report'
                sh 'docker stack rm test_character_stack'
            }
        }
    }
}