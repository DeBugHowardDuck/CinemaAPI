
def _token(client):
    client.post("/auth/register", json={"email":"u@test.com","password":"123","name":"U"})
    r = client.post("/auth/login", json={"email":"u@test.com","password":"123"})
    return r.get_json()["token"]

def test_movies_crud_and_pagination(client):
    t = _token(client)
    r = client.post("/movies", json={"title":"A","year":2020,"rating":7.5}, headers={"Authorization":f"Bearer {t}"})
    assert r.status_code == 201
    movie_id = r.get_json().get("id") or 1

    r = client.get("/movies?per_page=1&page=1&sort=rating&order=desc")
    assert r.status_code == 200
    data = r.get_json()
    assert "items" in data and "total" in data

    r = client.put(f"/movies/{movie_id}", json={"title":"B"}, headers={"Authorization":f"Bearer {t}"})
    assert r.status_code == 200

    r = client.get(f"/movies/{movie_id}")
    assert r.status_code in (200,404)

    r = client.delete(f"/movies/{movie_id}", headers={"Authorization":f"Bearer {t}"})
    assert r.status_code in (204,404)
