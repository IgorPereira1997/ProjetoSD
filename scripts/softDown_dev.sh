#!/usr/bin/env bash

docker compose -f docker-compose.yml down -v
docker network prune -f

rm -rf postgres_container/pgdata/
