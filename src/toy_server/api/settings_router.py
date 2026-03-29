from fastapi.routing import APIRouter
from config.settings import settings

router = APIRouter()

@router.get("/settings")
async def get_settings():
    return settings.model_dump()
