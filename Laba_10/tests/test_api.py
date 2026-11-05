import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_books_api(client):
    res = client.get("/books")
    assert res.status_code == 200
    assert len(res.get_json()) == 4


def test_get_single_book_api(client):
    res = client.get("/books/1")
    assert res.status_code == 200
    assert res.get_json()["title"] == "Война и мир"


def test_get_book_not_found(client):
    res = client.get("/books/999")
    assert res.status_code == 404
    assert res.get_json()["code"] == "NOT_FOUND"


def test_create_book_api(client):
    payload = {"title": "Новая книга", "author": "Автор", "year": 2023, "genre": "Наука", "price": 450.0}
    res = client.post("/books", json=payload)
    assert res.status_code == 201
    assert res.get_json()["id"] == 5


def test_patch_book_api(client):
    payload = {"price": 1500.0}
    res = client.patch("/books/1", json=payload)
    assert res.status_code == 200
    assert res.get_json()["price"] == 1500.0