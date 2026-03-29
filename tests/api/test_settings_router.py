from fastapi.testclient import TestClient
from config.settings import settings

def test_settings(client: TestClient) -> None:
    response = client.get("/settings")
    assert response.status_code == 200
    content = response.json()
    assert content == settings.model_dump()
