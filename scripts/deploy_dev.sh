#!/usr/bin/env bash

docker compose -f docker-compose.yml up -d --build --remove-orphans
#docker compose build
#docker compose up