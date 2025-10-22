
def test_protected_without_token(client):
    r = client.post("/movies", json={"title":"X","year":2024,"rating":8.1})
    assert r.status_code == 401
