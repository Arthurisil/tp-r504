#!/bin/bash

CONTAINER_NAME="tp4-app"
IMAGE_NAME="im-tp4"
NETWORK_NAME="net-tp4"
PORT="5000"

echo "Lancement du conteneur $CONTAINER_NAME"
docker run -d \
    --name $CONTAINER_NAME \
    --network $NETWORK_NAME \
    -p $PORT:$PORT \
    $IMAGE_NAME



