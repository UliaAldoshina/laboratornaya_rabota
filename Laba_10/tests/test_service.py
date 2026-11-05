import pytest
from repository import BookRepository
from service import BookService
from exceptions import BookNotFoundError, ValidationError


def test_service_get_books_filtered():
    repo = BookRepository()
    service = BookService(repo)

    result = service.get_books(genre="Роман")
    assert len(result) == 3


def test_service_create_invalid_price():
    repo = BookRepository()
    service = BookService(repo)

    data = {"title": "B", "author": "A", "year": 2020, "genre": "G", "price": -100}
    with pytest.raises(ValidationError):
        service.create_book(data)


def test_service_get_not_found():
    repo = BookRepository()
    service = BookService(repo)

    with pytest.raises(BookNotFoundError):
        service.get_book(999)