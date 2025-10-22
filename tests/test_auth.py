
def test_register_and_login(client):
    r = client.post("/auth/register", json={"email":"u@test.com","password":"123","name":"U"})
    assert r.status_code in (201,409)
    r = client.post("/auth/login", json={"email":"u@test.com","password":"123"})
    assert r.status_code == 200
    assert "token" in r.get_json()
