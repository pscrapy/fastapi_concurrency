#!/bin/bash

exec uvicorn toy_server.app:app \
    --host ${SERVER_HOST} --port ${SERVER_PORT} \
    --workers ${UVICORN_WORKERS} \
    --limit-concurrency ${UVICORN_CONCURRENCY_LIMIT} \
    --backlog ${UVICORN_BACKLOG}