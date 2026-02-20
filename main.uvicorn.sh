#!/bin/bash

exec uvicorn toy_server.app:app \
    --host ${SERVER_HOST} --port ${SERVER_PORT}