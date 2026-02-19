from fastapi.routing import APIRouter

router = APIRouter()

@router.get("/healthcheck")
async def health():
    return {"status": "OK"}