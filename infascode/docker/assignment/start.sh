#!/bin/bash

# stäng ner eventuella existerande containrar med samma namn
docker rm -f api persistance

# ta bort nätverket 'infra' om det existerar
docker network rm infra

# skapa nätverket 'infra' om det inte redan finns
if ! docker network ls | grep -q infra; then
    docker network create infra
fi

docker build -t todo-api -f Dockerfile.api .

docker run -d \
    --name persistance \
    --network infra \
    -e MYSQL_ROOT_PASSWORD=root \
    -e MYSQL_DATABASE=todo_db \
    -v $(pwd)/mysql_data:/var/lib/mysql \
    mysql:8.0

docker run -d \
    --name api \
    --network infra \
    -p 5000:5000 \
    -v $(pwd)/app.py:/app/app.py \
    -v $(pwd)/requirements.txt:/app/requirements.txt \
    todo-api
