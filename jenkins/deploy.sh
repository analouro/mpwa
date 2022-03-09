#!/bin/bash

echo "Deploy stage"

ssh jenkins@ana-machine docker stack deploy --compose-file docker-compose.yaml mpwa