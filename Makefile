PROJ_PATH=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))
WEB_APP_PATH = src/mimir
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
	black ${APP_PATH} && isort ${APP_PATH} && mypy ${APP_PATH}
