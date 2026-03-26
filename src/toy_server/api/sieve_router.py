from asyncer import asyncify

from fastapi import Request
from fastapi.routing import APIRouter

from toy_server.core.sieve import prime_sieve

router = APIRouter(prefix="/api/sieve")


@router.get("/def")
def def_sieve(n: int):
    nth_prime = prime_sieve(n)
    return {
        "nth_prime" : nth_prime
    }


@router.get("/async")
async def def_sieve(n: int):
    nth_prime = await asyncify(prime_sieve)(n)
    return {
        "nth_prime" : nth_prime
    }
