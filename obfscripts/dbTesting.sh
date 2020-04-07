#!/bin/bash
source /var/bin/jenkins/workspace/sfia_project_2/sourcetest.env
python3 -m coverage run -m pytest tests/db_testing.py
python3 -m coverage report