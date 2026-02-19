test:
	poetry run pytest

build-base: test
	docker build -f docker/Dockerfile.base --tag fastapi_concurrency_base:latest .

# FASTAPI CLI
build-fastapi: build-base
	docker build -f docker/Dockerfile.fastapi --tag fastapi_concurrency:fastapi .

run-fastapi: build-fastapi
	docker run --rm --publish 127.0.0.1:8080:8080 fastapi_concurrency:fastapi 

# GUNICORN
build-gunicorn: build-base
	docker build -f docker/Dockerfile.gunicorn --tag fastapi_concurrency:gunicorn .

run-gunicorn: build-gunicorn
	docker run --rm --publish 127.0.0.1:8080:8080 fastapi_concurrency:gunicorn 

# MAIN
build-main: build-base
	docker build -f docker/Dockerfile.main --tag fastapi_concurrency:main .

run-main: build-main
	docker run --rm --publish 127.0.0.1:8080:8080 fastapi_concurrency:main 

# UVICORN
build-uvicorn: build-base
	docker build -f docker/Dockerfile.uvicorn --tag fastapi_concurrency:uvicorn .

run-uvicorn: build-uvicorn
	docker run --rm --publish 127.0.0.1:8080:8080 fastapi_concurrency:uvicorn 


build-all: build-uvicorn build-main build-fastapi build-gunicorn


clean:
	docker image prune -f