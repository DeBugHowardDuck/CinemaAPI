
import os
import pytest
from app import create_app
from app.extensions.extensions import db

@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("DATABASE_URI", "sqlite:///:memory:")
    monkeypatch.setenv("JWT_SECRET", "test-secret")
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as c:
        with app.app_context():
            db.create_all()
        yield c
