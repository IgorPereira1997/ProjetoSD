# syntax=docker/dockerfile:1
FROM ubuntu:latest

COPY requirements.txt /code/

RUN apt update && apt install libmagic1
RUN python3 -m pip install -r requirements.txt --no-cache-dir

COPY . /code/
