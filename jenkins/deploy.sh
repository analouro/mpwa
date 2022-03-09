#!/bin/bash

echo "Deploy stage"

# copying docker-compose.yaml to swarm machine
scp docker-compose.yaml jenkins@ana-swarm:/home/jenkins/docker-compose.yaml

ssh jenkins@ana-swarm \
    DOCKER_HUB_CREDS_USR=$DOCKER_HUB_CREDS_USR docker stack deploy --compose-file docker-compose.yaml mpwa