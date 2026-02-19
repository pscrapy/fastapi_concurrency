from fastapi.testclient import TestClient


def test_sieve_def(client: TestClient) -> None:
    response = client.get("/api/sieve/def?n=5")
    assert response.status_code == 200
    content = response.json()
    assert content["nth_prime"] == 11


def test_sieve_def_long(client: TestClient) -> None:
    response = client.get("/api/sieve/def?n=100000")
    assert response.status_code == 200
    content = response.json()
    assert content["nth_prime"] == 1299709


def test_sieve_async(client: TestClient) -> None:
    response = client.get("/api/sieve/async?n=5")
    assert response.status_code == 200
    content = response.json()
    assert content["nth_prime"] == 11


def test_sieve_async_long(client: TestClient) -> None:
    response = client.get("/api/sieve/async?n=100000")
    assert response.status_code == 200
    content = response.json()
    assert content["nth_prime"] == 1299709