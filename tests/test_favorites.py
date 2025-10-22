
def _token(client):
    client.post("/auth/register", json={"email":"u2@test.com","password":"123","name":"U2"})
    r = client.post("/auth/login", json={"email":"u2@test.com","password":"123"})
    return r.get_json()["token"]

def test_favorites_add_remove(client):
    t = _token(client)
    r = client.post("/movies", json={"title":"Fav","year":2021,"rating":6.2}, headers={"Authorization":f"Bearer {t}"})
    assert r.status_code == 201
    movie_id = r.get_json().get("id") or 1
    r = client.post(f"/favorites/1/{movie_id}", headers={"Authorization":f"Bearer {t}"})
    assert r.status_code == 204
    r = client.delete(f"/favorites/1/{movie_id}", headers={"Authorization":f"Bearer {t}"})
    assert r.status_code == 204
