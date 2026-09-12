
import sys
import asyncio
from fastapi.routing import APIRouter
from fastapi import BackgroundTasks

from toy_server.core.seppuku.memory import SizeUnit, generate_footprint
from toy_server.core.seppuku.threads import busywork

# NB registries are scoped to single worker process
OBJECT_REGISTRY = list()
THREAD_REGISTRY = {
    "threads": 0,
    "background": 0
}


router = APIRouter(prefix="/api/seppuku")

@router.post("/memory")
def memory_growth(n: int, unit: SizeUnit):

    new_obj = generate_footprint(n, unit)

    OBJECT_REGISTRY.append(new_obj)
    
    return {"new_obj": sys.getsizeof(new_obj)}


@router.get("/memory")
async def memory_status():
    return {
        "memory": [ sys.getsizeof(x) for x in OBJECT_REGISTRY ]
    }



@router.post("/thread")
def thread_spawner(background_tasks: BackgroundTasks, bkg: bool = False):

    if bkg:
        background_tasks.add_task(busywork)
        THREAD_REGISTRY["background"] += 1
        return {"new_task": "BACKGROUND"}
    else:
        coro = asyncio.to_thread(busywork)
        THREAD_REGISTRY["threads"] += 1
        return {"new_task": "THREAD"}



@router.get("/thread")
def thread_status():
    return THREAD_REGISTRY