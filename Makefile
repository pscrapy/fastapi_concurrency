#!make
include config.env

ARCH = $$(arch)

test:
	poetry run pytest

build-base: test
	docker build -f docker/Dockerfile.base --tag fastapi_concurrency_base:latest .

# FASTAPI CLI
build-fastapi: build-base
	docker build -f docker/Dockerfile.fastapi --tag fastapi_concurrency:fastapi-${ARCH} .

run-fastapi:
	docker run --rm --env-file=config.env --publish 127.0.0.1:${SERVER_PORT}:${SERVER_PORT} fastapi_concurrency:fastapi-${ARCH}

# GUNICORN
build-gunicorn: build-base
	docker build -f docker/Dockerfile.gunicorn --tag fastapi_concurrency:gunicorn-${ARCH} .

run-gunicorn:
	docker run --rm --env-file=config.env --publish 127.0.0.1:${SERVER_PORT}:${SERVER_PORT} fastapi_concurrency:gunicorn-${ARCH}

# MAIN
build-main: build-base
	docker build -f docker/Dockerfile.main --tag fastapi_concurrency:main-${ARCH} .

run-main:
	docker run --rm --env-file=config.env --publish 127.0.0.1:${SERVER_PORT}:${SERVER_PORT} fastapi_concurrency:main-${ARCH}

# UVICORN
build-uvicorn: build-base
	docker build -f docker/Dockerfile.uvicorn --tag fastapi_concurrency:uvicorn-${ARCH} .

run-uvicorn:
	docker run --rm --env-file=config.env --publish 127.0.0.1:${SERVER_PORT}:${SERVER_PORT} fastapi_concurrency:uvicorn-${ARCH}


build-all: build-uvicorn build-main build-fastapi build-gunicorn


tag-all:
	docker tag fastapi_concurrency:gunicorn-${ARCH} pscrapy/test_fastapi_concurrency:gunicorn-${ARCH}
	docker tag fastapi_concurrency:main-${ARCH} pscrapy/test_fastapi_concurrency:main-${ARCH}
	docker tag fastapi_concurrency:fastapi-${ARCH} pscrapy/test_fastapi_concurrency:fastapi-${ARCH}
	docker tag fastapi_concurrency:uvicorn-${ARCH} pscrapy/test_fastapi_concurrency:uvicorn-${ARCH}

push-tags: tag-all
	docker push pscrapy/test_fastapi_concurrency:gunicorn-${ARCH}
	docker push pscrapy/test_fastapi_concurrency:main-${ARCH}
	docker push pscrapy/test_fastapi_concurrency:fastapi-${ARCH}
	docker push pscrapy/test_fastapi_concurrency:uvicorn-${ARCH}


clean:
	docker image prune -f