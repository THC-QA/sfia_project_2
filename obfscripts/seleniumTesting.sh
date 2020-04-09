#!/bin/bash
source ~/.bashrc
python3 -m coverage run -m pytest tests/selenium_testing.py
python3 -m coverage report