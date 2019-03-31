FROM ubuntu:16.04

FROM python:3.6.5

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip

RUN pip --default-timeout=100 install -r requirements.txt

COPY . /app

CMD python /app/model.py && python /app/server.py