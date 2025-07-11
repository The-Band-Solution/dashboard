up:
	docker-compose up
build:
	docker-compose up --build
down:
	docker-compose down
destroy:
	docker-compose down -v
superuser:
	sh ./create_superuser.sh

