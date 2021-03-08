FROM debian:buster

RUN apt update -y

RUN apt install -y python-pip git

RUN pip install flask

RUN git clone https://github.com/thewarsawpakt/flask_auth

RUN cd flask_auth

RUN python -m flask_auth