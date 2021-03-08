FROM debian:buster

RUN apt update -y

RUN apt install -y python-pip 

RUN pip install flask

RUN python -m flask_auth 