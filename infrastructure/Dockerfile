ARG PYTHON_VERSION=3.12.1

FROM python:${PYTHON_VERSION} as core
ARG APP_DIR=/sites/app/
ENV APP_DIR=${APP_DIR} \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_COMPILE=0 \
    PYTHONPATH="${APP_DIR}:${PYTHONPATH}" \
    PATH="/root/.local/bin:${APP_DIR}/infrastructure/bin:${PATH}"

WORKDIR ${APP_DIR}

RUN apt update -y && apt upgrade -y # For psycopg2
RUN apt install -y libpq-dev # For psycopg2

COPY infrastructure ${APP_DIR}/infrastructure
COPY application ${APP_DIR}/application
COPY interface ${APP_DIR}/interface

RUN python3.12 -m pip install --user --no-cache-dir -r ${APP_DIR}/infrastructure/requirements/requirements.txt

RUN chmod +x ${APP_DIR}/infrastructure/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]
