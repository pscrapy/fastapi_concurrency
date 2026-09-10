from fastapi import FastAPI

from toy_server.api.health_router import router as health_router
from toy_server.api.sieve_router import router as sieve_router
from toy_server.api.seppuku_router import router as seppuku_router
from toy_server.api.settings_router import router as settings_router

app = FastAPI()

app.include_router(health_router)
app.include_router(sieve_router)
app.include_router(settings_router)
app.include_router(seppuku_router)
