#!/bin/bash

# Nome do container Django
CONTAINER_NAME="dashboard_the_band"

# Caminho do script Python dentro do container
SCRIPT_PATH="/app/src/create_superuser.py"

echo "Executando criação de superusuário no container $CONTAINER_NAME..."

docker exec -it "$CONTAINER_NAME" python "$SCRIPT_PATH"
