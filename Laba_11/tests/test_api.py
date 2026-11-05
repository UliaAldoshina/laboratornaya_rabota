import pytest
from app import app, repo

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_api_get_books(client):
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_api_book_not_found(client):
    response = client.get("/books/9999")
    assert response.status_code == 404
    data = response.get_json()
    assert data["code"] == "NOT_FOUND"