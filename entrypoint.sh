#!/bin/bash
set -e

echo "Aguardando PostgreSQL..."
while ! nc -z db 5432; do
  sleep 1
done
echo "PostgreSQL está pronto!"


echo "Executando make migrations..."
python manage.py makemigrations

echo "Executando migrations..."
python manage.py migrate

echo "Iniciando aplicação..."
exec "$@"
