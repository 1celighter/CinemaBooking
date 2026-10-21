from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

payload = {"MovieName": "testing"}


def test_get_movie_catalog():
    response = client.get("/MoviesCatalog")
    assert response.status_code == 200
    assert response.json()["Movies"] == []

def test_get_movie_ById(): # also we need use rule AAA (Arrange -> Act -> Assert)
    # 1 - Arrange     
    payload = {
        "MID": 1,
        "MovieName": "patro",
        "MovieStudio": "WayGave studios",
        "StudioEmail": "WayGaveSt@gmail.com",
        "MetaCriticScore": 9.2,
        "UserScore": 83,
        "ContentRating": 18,
        "MovieGenre": "Detective"
    }
    add_response = client.post("/AddMovie", json=payload)
    assert add_response.status_code == 201

    created_mid = add_response.json()["Movie Status"]["MID"]
    # 2 - Act
    response = client.get(f"/Movies/{created_mid}")

    # 3 - Assert 
    assert response.status_code == 200
    assert response.json()["Movie"]["MID"] == created_mid
    assert response.json()["Movie"]["Movie Name"] == "patro"

def test_get_by_wrong_id():
    response = client.get("/Movies/11111")
    assert response.status_code == 404
    assert response.json()["detail"] == "Movie with this 11111 Id has not found"

def test_add_movie():
    response = client.post("/AddMovie", json=payload)
    assert response.status_code == 422
    assert "detail" in response.json()

