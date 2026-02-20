#!/bin/bash

exec gunicorn toy_server.app:app \
    -w 4 \
    -k uvicorn_worker.UvicornWorker \
    --bind ${SERVER_HOST}:${SERVER_PORT}