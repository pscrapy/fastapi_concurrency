from typing import Generator

import pytest
from fastapi.testclient import TestClient

from toy_server.app import app


@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)