from fastapi import FastAPI

from toy_server.api.health_router import router as health_router
from toy_server.api.sieve_router import router as sieve_router

app = FastAPI()

app.include_router(health_router)
app.include_router(sieve_router)
