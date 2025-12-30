from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_banks():
    response = client.get("/banks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_invalid_branch():
    response = client.get("/branches/NONEXISTENT123")
    assert response.status_code == 404