down:
	docker-compose -f infrastructure/compose.yaml down

up:
	docker-compose -f infrastructure/compose.yaml up -d

build:
	docker-compose -f infrastructure/compose.yaml up -d --build

logs:
	docker-compose -f infrastructure/compose.yaml logs -f

bash:
	docker-compose -f infrastructure/compose.yaml exec backend bash

dv:
	docker-compose -f infrastructure/compose.yaml down -v

restart: down up
rebuild: down build
