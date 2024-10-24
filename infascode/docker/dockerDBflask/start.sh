#!/bin/bash

docker network create infra

docker build -t mydb -f Dockerfile.persistance .

docker run -d --name db --network infra -v data:/var/lib/mysql -e MYSQL_DATABASE=mydatabase -e MYSQL_USER=myuser -e MYSQL_PASSWORD=mypassword -e MYSQL_ROOT_PASSWORD=rootpassword mydb

docker build -t myapi -f Dockerfile.api .

docker run -d --name api --network infra -v "$(pwd)":/app -p 5000:5000 myapi
