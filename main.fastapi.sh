#!/bin/bash

exec fastapi run src/toy_server/app.py \
    --port ${SERVER_PORT} \
    --workers ${FASTAPI_WORKERS}