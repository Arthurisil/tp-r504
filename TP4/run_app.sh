#!/bin/bash

CONTAINER_NAME="tp4-app"
IMAGE_NAME="im-tp4"
NETWORK_NAME="net-tp4"
PORT="5000"

# Vérifier si existe déjà
if [ $(docker ps -a -q -f name=$CONTAINER_NAME) ]; then
    echo "$CONTAINER_NAME existe déjà, il va être supprimé"
    docker rm -f $CONTAINER_NAME
fi

# Lancer le new conteneur
echo "Lancement du conteneur $CONTAINER_NAME"
docker run -d \
    --name $CONTAINER_NAME \
    --network $NETWORK_NAME \
    -p $PORT:$PORT \
    $IMAGE_NAME

# Affiche le statut 
docker ps -f name=$CONTAINER_NAME

