DC = docker compose
BACKEND_CONTAINER = backend1

PHONY: up down build bash logs docs

up:
	${DC} up -d

down:
	${DC} down

build:
	${DC} build

bash:
	${DC} exec -it ${BACKEND_CONTAINER} bash

logs:
	${DC} logs ${BACKEND_CONTAINER}

docs:
	${DC} --profile docs up -d
