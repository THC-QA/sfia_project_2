pipeline{
    agent none

    stages{
        stage("testEnv"){
            agent {label 'master'}
            steps{
                sh 'echo "dev-test local install"'
                // sh 'sudo apt update -y'
                // sh 'sudo apt-get remove docker docker-engine docker.io -y'
                // sh 'sudo apt-get purge containderd.io docker.io'
                // sh 'sudo apt-get install containerd.io'
                // sh 'sudo apt install docker.io -y'
                // sh 'sudo apt install docker-compose -y'
                // sh 'sudo systemctl start docker'
                // sh 'sudo systemctl enable docker'
                // sh 'sudo systemctl status docker'
                // sh 'sudo usermod -aG docker $USER'
                // sh 'sudo apt install software-properties-common'
                // sh 'sudo apt-add-repository --yes --update ppa:ansible/ansible'
                // sh 'sudo apt install ansible -y'
                // sh 'ansible --version'
            }
        }
        stage("testingInstall"){
            agent {label 'master'}
            steps{
                sh 'echo "install testing dependencies"'
                sh 'chmod +x /var/lib/jenkins/workspace/sfia_project_2/obfscripts/*'
                sh './obfscripts/testingInstall.sh'
                sh 'sleep 20'
            }
        }
        stage("urlTesting"){
            agent {label 'master'}
            steps{
                sh 'echo "Pinging URLs"'
                sh 'chmod +x /var/lib/jenkins/workspace/sfia_project_2/obfscripts/*'
                sh 'python3 -m coverage run -m pytest tests/url_testing.py'
                sh 'python3 -m coverage report'
            }

        }
        stage("dbTesting"){
            agent {label 'master'}
            steps{
                sh 'echo "Probing MySQL Database"'
                sh './obfscripts/dbTesting.sh'
            }
        }
        stage("seleniumTesting"){
            agent {label 'master'}
            steps{
                sh 'echo "Mining the Selenium"'
                // sh 'python3 -m coverage run -m pytest tests/selenium_testing.py'
                // sh 'python3 -m coverage report'
                sh 'docker stack rm test_character_stack'
            }
        }
        stage("ansibleSetup"){
            agent {label 'master'}
            steps{
                sh 'echo "Antsy Ansible"'
                sh 'chmod +x /var/lib/jenkins/workspace/sfia_project_2/obfscripts/*'
                sh './obfscripts/ansibleSetup.sh'
            }
        }
        stage("swarmDeploy"){
            agent {label 'manager-node'}
            steps{
                sh 'newgrp docker'
                sh 'docker stack rm character_stack'
                sh 'docker stack deploy --compose-file docker-compose.yml character_stack'
            }
        }
    }
}