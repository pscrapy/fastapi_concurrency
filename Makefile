#!make
include config.env

test:
	poetry run pytest

build-base: test
	docker build -f docker/Dockerfile.base --tag fastapi_concurrency_base:latest .

# FASTAPI CLI
build-fastapi: build-base
	docker build -f docker/Dockerfile.fastapi --tag fastapi_concurrency:fastapi .

run-fastapi:
	docker run --rm --env-file=config.env --publish 127.0.0.1:${SERVER_PORT}:${SERVER_PORT} fastapi_concurrency:fastapi 

# GUNICORN
build-gunicorn: build-base
	docker build -f docker/Dockerfile.gunicorn --tag fastapi_concurrency:gunicorn .

run-gunicorn:
	docker run --rm --env-file=config.env --publish 127.0.0.1:${SERVER_PORT}:${SERVER_PORT} fastapi_concurrency:gunicorn 

# MAIN
build-main: build-base
	docker build -f docker/Dockerfile.main --tag fastapi_concurrency:main .

run-main:
	docker run --rm --env-file=config.env --publish 127.0.0.1:${SERVER_PORT}:${SERVER_PORT} fastapi_concurrency:main 

# UVICORN
build-uvicorn: build-base
	docker build -f docker/Dockerfile.uvicorn --tag fastapi_concurrency:uvicorn .

run-uvicorn:
	docker run --rm --env-file=config.env --publish 127.0.0.1:${SERVER_PORT}:${SERVER_PORT} fastapi_concurrency:uvicorn 


build-all: build-uvicorn build-main build-fastapi build-gunicorn


tag-all:
	docker tag fastapi_concurrency:gunicorn pscrapy/test_fastapi_concurrency:gunicorn
	docker tag fastapi_concurrency:main pscrapy/test_fastapi_concurrency:main
	docker tag fastapi_concurrency:fastapi pscrapy/test_fastapi_concurrency:fastapi
	docker tag fastapi_concurrency:uvicorn pscrapy/test_fastapi_concurrency:uvicorn

push-tags:
	docker push pscrapy/test_fastapi_concurrency:gunicorn
	docker push pscrapy/test_fastapi_concurrency:main
	docker push pscrapy/test_fastapi_concurrency:fastapi
	docker push pscrapy/test_fastapi_concurrency:uvicorn
	

clean:
	docker image prune -f