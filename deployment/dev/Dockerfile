# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Potery
ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VERSION=1.3.2 \
    POETRY_VENV=/opt/poetry-venv \
    POETRY_CACHE_DIR=/opt/.cache

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

RUN apt-get update && apt-get install make git python3-dev libpq-dev gcc curl -y --no-install-recommends 

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

WORKDIR /app

COPY ./poetry.lock ./pyproject.toml /

# Install requirements
RUN poetry install

COPY . /app

# Set python path
ENV PYTHONPATH "${PYTHONPATH}:${PWD}/app/src/mimir/web_app:${PWD}/app/src/"

# Copy script to run app and set permissions
COPY ./deployment/dev/start.sh /start.sh
RUN chmod +x /start.sh

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
