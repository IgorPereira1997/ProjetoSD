#!/usr/bin/env bash

docker compose down -v
docker system prune -f -a
docker volume prune -f
docker network prune -f

rm -rf postgres_container/pgdata/
