FROM python:3-slim

RUN apt update && apt install nano curl -y

WORKDIR /server_1

COPY ./src /server_1

COPY requirements.txt /server_1/

RUN pip install -r requirements.txt

RUN groupadd -r minhph && useradd -r -g minhph -s /sbin/nologin minhph

USER minhph

CMD python server_1.py
