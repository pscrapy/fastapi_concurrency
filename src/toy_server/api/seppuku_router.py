
import sys
import asyncio
from fastapi.routing import APIRouter
from fastapi import BackgroundTasks

from toy_server.core.seppuku.memory import SizeUnit, generate_footprint
from toy_server.core.seppuku.threads import busywork, sleepywork, TaskType, ThreadType

# NB registries are scoped to single worker process
OBJECT_REGISTRY = list()
THREAD_REGISTRY = {
    ThreadType.THREAD: {
        TaskType.SLEEPY: 0,
        TaskType.BUSY: 0
    },
    ThreadType.BACKGROUND: {
        TaskType.SLEEPY: 0,
        TaskType.BUSY: 0
    }
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
def thread_spawner(background_tasks: BackgroundTasks, bkg: bool = False, sleepy: bool = False):

    task = sleepywork if sleepy else busywork   
    key = TaskType.SLEEPY if sleepy else TaskType.BUSY
    
    thread_type = ThreadType.BACKGROUND if bkg else ThreadType.THREAD

    if bkg:
        background_tasks.add_task(task)
    else:
        coro = asyncio.to_thread(task)
    
    THREAD_REGISTRY[thread_type][key] += 1
    return {
        "new_task": thread_type,
        "type": key
    }



@router.get("/thread")
def thread_status():
    return THREAD_REGISTRY