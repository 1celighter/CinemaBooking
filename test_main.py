from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

payload = {"MovieName": "testing"}


def test_get_movie_catalog():
    response = client.get("/MoviesCatalog")
    assert response.status_code == 200
    assert response.json()["Movies"] == []


def test_add_movie():
    response = client.post("/AddMovie", json=payload)
    assert response.status_code == 422
    assert "detail" in response.json()
