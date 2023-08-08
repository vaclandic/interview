FROM python:3

RUN apt-get update && apt-get install nginx -y
COPY src /src

WORKDIR /src

RUN pip3 install -r requirements.txt

