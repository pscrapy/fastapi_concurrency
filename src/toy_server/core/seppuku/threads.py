import time
from enum import StrEnum


class TaskType(StrEnum):
    SLEEPY = "sleepy"
    BUSY = "busy"


class ThreadType(StrEnum):
    BACKGROUND = "background"
    THREAD = "thread"


def busywork():
    x = 1
    while True:
        x *= -1


def sleepywork():
    while True:
        time.sleep(10)
