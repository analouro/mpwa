#!/bin/bash

echo "Deploy stage"

ssh jenkins@ana-swarm docker stack deploy --compose-file docker-compose.yaml mpwa