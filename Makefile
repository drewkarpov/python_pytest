PROJECT_PATH ?= $(shell pwd)
HOST ?= $(shell ifconfig | grep 'inet ' | grep -v '127.0.0.1' | awk '{print $2}')

run_application:
	make run_selenoid
	PROJECT_PATH=$(PROJECT_PATH) docker-compose stop application
	PROJECT_PATH=$(PROJECT_PATH) docker-compose up --build -d application

run_selenoid:
	PROJECT_PATH=$(PROJECT_PATH) docker-compose stop selenoid
	PROJECT_PATH=$(PROJECT_PATH) docker-compose up --build -d selenoid

run_tests:
	make run_application
	HOST=$(HOST) pytest test_framework/tests
