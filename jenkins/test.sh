#!/bin/bash

echo "Test stage"

# create venv
python3 -m venv venv
source venv/bin/activate

# cd flask-app
cd flask-app

# install requirements.txt
pip3 install -r requirements.txt

# run pytest
python3 -m pytest --cov-report term-missing