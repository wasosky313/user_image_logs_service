FROM python:3.8-slim-buster

ARG DB_HOST="localhost"
ARG MQ_CONNECTION="localhost"

RUN pip3 install --upgrade pip

COPY . /api

WORKDIR /api

RUN pip3 install -e .

ENV DB_HOST=$DB_HOST
ENV MQ_CONNECTION=$MQ_CONNECTION

WORKDIR /api/worker

CMD ["python", "main.py"]