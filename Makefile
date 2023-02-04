PROJ_PATH=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))
PPATH = ${PYTHONPATH}:${PWD}/src/mimir/web_app:${PWD}/src/
WEB_APP_PATH = src/mimir/web_app
APP_PATH = src/
TEST_PATH = tests/
PYTHON_EXEC?=poetry run python
ADMIN_EMAIL?=admin@mimir.com
ADMIN_PASS?=admin


# Django App
run:
	poetry run python ${WEB_APP_PATH}/manage.py runserver

create_admin:
	$(PYTHON_EXEC) ${WEB_APP_PATH}/manage.py create_admin --password ${ADMIN_PASS} --noinput --email ${ADMIN_EMAIL}

collectstatic:
	$(PYTHON_EXEC) ${WEB_APP_PATH}/manage.py collectstatic --noinput

migrate:
	$(PYTHON_EXEC) ${WEB_APP_PATH}/manage.py createcachetable # Like migrate, createcachetable won’t touch an existing table. It will only create missing tables.
	$(PYTHON_EXEC) ${WEB_APP_PATH}/manage.py migrate

makemigrations:
	$(PYTHON_EXEC) ${WEB_APP_PATH}/manage.py makemigrations infrastructure

# Linting
lint:
	poetry run black ${APP_PATH} ${TEST_PATH} && poetry run isort ${APP_PATH} ${TEST_PATH} && poetry run mypy ${APP_PATH}

# Tests
test:
	${PYTHON_EXEC} pytest tests
