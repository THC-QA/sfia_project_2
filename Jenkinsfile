pipeline{
    agent none

    stages{
        stage("testEnv"){
            agent {label 'master'}
            steps{
                sh 'echo "dev-test local install"'
                // sh 'sudo apt update -y'
                // sh 'sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4'
                // sh 'sudo apt-get install default-jdk'
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
                sh 'chmod +x /var/lib/jenkins/workspace/sfia_project_2/obfscripts/testingInstall.sh'
                sh './obfscripts/testingInstall.sh'
                sh 'sleep 15'
            }
        }
        stage("urlTesting"){
            agent {label 'master'}
            steps{
                sh 'echo "Pinging URLs"'
                sh 'python3 -m coverage run -m pytest tests/url_testing.py'
                sh 'python3 -m coverage report'
            }

        }
        stage("dbTesting"){
            agent {label 'master'}
            steps{
                sh 'echo "Probing MySQL Database"'
                sh 'chmod +x /var/lib/jenkins/workspace/sfia_project_2/obfscripts/dbTesting.sh'
                sh './obfscripts/dbTesting.sh'
            }
        }
        stage("seleniumTesting"){
            agent {label 'master'}
            steps{
                sh 'echo "Mining the Selenium"'
                sh 'chmod +x /var/lib/jenkins/workspace/sfia_project_2/obfscripts/seleniumTesting.sh'
                sh './obfscripts/seleniumTesting.sh'
                sh 'docker stack rm test_character_stack'
            }
        }
        stage("ansibleSetup"){
            agent {label 'master'}
            steps{
                sh 'echo "Antsy Ansible"'
                sh 'chmod +x /var/lib/jenkins/workspace/sfia_project_2/obfscripts/ansibleSetup.sh'
                sh './obfscripts/ansibleSetup.sh'
            }
        }
        stage("swarmDeploy"){
            agent {label 'manager-node'}
            steps{
                // sh 'newgrp docker'
                // sh 'sudo docker stack rm character_stack'
                // sh 'sleep 15'
                sh 'sudo docker stack deploy --compose-file docker-compose.yml character_stack'
            }
        }
    }
}