#!/bin/bash
# sudo apt install python3-venv -y
# python3 -m venv venv
source venv/bin/activate
# pip3 install pytest
# pip3 install coverage
# pip3 install -r /var/lib/jenkins/workspace/sfia_project_2/requirements.txt
# pip3 install -U selenium
docker swarm leave -f
docker swarm init
docker stack deploy --compose-file /var/lib/jenkins/workspace/sfia_project_2/docker-testing-compose.yml test_character_stack