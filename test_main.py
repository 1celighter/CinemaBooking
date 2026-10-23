from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

payload = {"MovieName": "testing"}


def test_get_movie_catalog():
    response = client.get("/Movies")
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
    add_response = client.post("Movies/Add", json=payload)
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
    assert response.json()["detail"] == "Movie with this 11111 id has not found"

def test_add_movie():
    response = client.post("Movies/Add", json=payload)
    assert response.status_code == 422
    assert "detail" in response.json()

def test_update_movie():
    payload = {
        "MID": 1,
        "MovieName": "Initial Title",
        "MovieStudio": "WayGave studios",
        "StudioEmail": "WayGaveSt@gmail.com",
        "MetaCriticScore": 8,
        "UserScore": 80,
        "ContentRating": 16,
        "MovieGenre": "Action",
    }
    add_response = client.post("/Movies/Add",json=payload)
    created_mid = add_response.json()["Movie Status"]["MID"]

    updated_payload = {
        "MID": created_mid,
        "MovieName": "Updated Title",  # Поменяли название
        "MovieStudio": "WayGave studios",
        "StudioEmail": "WayGaveSt@gmail.com",
        "MetaCriticScore": 4.9,  # Поменяли оценку
        "UserScore": 85,
        "ContentRating": 16,
        "MovieGenre": "Action",
    }

    response = client.put(f"/Movies/Update/{created_mid}", json=updated_payload)
    assert response.status_code == 200

    get_response = client.get(f"/Movies/{created_mid}")

    assert get_response.status_code == 200
    assert get_response.json()["Movie"]["MovieName"] == "Updated Title"


def test_delete_movie():
    payload = {
        "MID": 1,
        "MovieName": "Movie To Delete",
        "MovieStudio": "WayGave studios",
        "StudioEmail": "WayGaveSt@gmail.com",
        "MetaCriticScore": 7,
        "UserScore": 70,
        "ContentRating": 12,
        "MovieGenre": "Comedy",
    }
    add_res = client.post("/Movies/Add", json=payload)
    created_mid = add_res.json()["Movie Status"]["MID"]

    delete_res = client.delete(f"/Movies/Delete/{created_mid}")
    assert delete_res.status_code in (200, 204)
    get_res = client.get(f"/Movies/{created_mid}")
    assert get_res.status_code == 404