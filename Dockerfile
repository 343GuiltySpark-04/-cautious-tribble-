# syntax=docker/dockerfile:1

FROM python:3.9.7-slim-buster

WORKDIR /app

COPY . .

CMD ["python", "./main.py"]