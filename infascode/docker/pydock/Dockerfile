FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install Flask --break-system-packages

WORKDIR /app

COPY app.py .

CMD ["flask", "--app", "/app/app.py", "run"]

#EXPOSE 5000 <- indicates that the container listens on the specified network ports at runtime
#USER <user> <- sets the user name or UID to use when running the image
