import uvicorn
from toy_server.app import app
from config.settings import settings

if __name__ == "__main__":
    uvicorn.run(
        app, 
        host=settings.server_host, port=settings.server_port, 
        workers=settings.uvicorn_workers,
        limit_concurrency=settings.uvicorn_concurrency_limit,
        backlog=settings.uvicorn_backlog
    )