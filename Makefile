PROJECT_PATH ?= $(shell pwd)

run_application:
	make run_selenoid
	PROJECT_PATH=$(PROJECT_PATH) docker-compose stop application
	PROJECT_PATH=$(PROJECT_PATH) docker-compose up --build -d application

run_selenoid:
	PROJECT_PATH=$(PROJECT_PATH) docker-compose stop selenoid
	PROJECT_PATH=$(PROJECT_PATH) docker-compose up --build -d selenoid