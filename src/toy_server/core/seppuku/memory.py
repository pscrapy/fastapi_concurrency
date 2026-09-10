from enum import StrEnum, Enum
from random import randbytes

class SizeUnit(StrEnum):
    KB = "KB"
    MB = "MB"
    GB = "GB"

K_SIZE = 1000
M_SIZE = 1000000


def generate_footprint(n: int, unit: SizeUnit):

    match unit:

        case SizeUnit.KB:
            size = n * K_SIZE
            random_bytes = randbytes(size)
        case SizeUnit.MB:
            size = n * M_SIZE
            random_bytes = randbytes(size)
        case SizeUnit.GB:
            random_bytes = b""
            steps = n * 10
            for _ in range(steps):
                random_bytes += randbytes(100 * M_SIZE)
        case _:
            raise RuntimeError(f"Unexpected unit {unit}")

    
    return random_bytes