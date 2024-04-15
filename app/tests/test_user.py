from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/users/")
    assert response.json() == [{"username": "Rick"}, {"username": "Morty"}]
    assert response.status_code == 200