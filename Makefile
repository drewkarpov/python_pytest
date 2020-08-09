PROJECT_PATH ?= $(shell pwd)

run_application:
	make run_selenoid
	make run_allure
	PROJECT_PATH=$(PROJECT_PATH) docker-compose stop application
	PROJECT_PATH=$(PROJECT_PATH) docker-compose up --build -d application

run_selenoid:
	PROJECT_PATH=$(PROJECT_PATH) docker-compose stop selenoid
	PROJECT_PATH=$(PROJECT_PATH) docker-compose up --build -d selenoid

run_allure:
	PROJECT_PATH=$(PROJECT_PATH) docker-compose stop allure
	PROJECT_PATH=$(PROJECT_PATH) docker-compose up -d allure

run_tests:
	make run_application
	flake8 --ignore=E501,W293,E731,W605,F405,F403,E402 test_framework
	HOST=$(HOST) pytest test_framework/tests --alluredir=allure/allure-results


hosting_allure_report:
	PROJECT_PATH=$(PROJECT_PATH) docker-compose stop allure_report
	PROJECT_PATH=$(PROJECT_PATH) docker-compose up --build -d allure_report
