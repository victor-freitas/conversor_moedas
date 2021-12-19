FROM python:3

WORKDIR /app

RUN apt-get update \
    apt-get install -y \
    python3 \
    python3-pip


COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD python3 run.py

