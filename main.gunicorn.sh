#!/bin/bash

exec gunicorn toy_server.app:app \
    --workers ${GUNICORN_WORKERS} \
    --worker-connections ${GUNICORN_WORKER_CONNECTIONS} \
    --backlog ${GUNICORN_BACKLOG} \
    -k uvicorn_worker.UvicornWorker \
    --bind ${SERVER_HOST}:${SERVER_PORT} 