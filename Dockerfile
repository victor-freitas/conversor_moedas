FROM ubuntu:20.04

WORKDIR /app

RUN apt-get update\
    python3\
    python3-pip

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt

CMD python3 run.py