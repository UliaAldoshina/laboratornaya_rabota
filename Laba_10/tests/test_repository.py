from repository import BookRepository
from models import Book


def test_repository_get_all_and_by_id():
    repo = BookRepository()
    books = repo.get_all()
    assert len(books) == 4

    book = repo.get_by_id(1)
    assert book is not None
    assert book.title == "Война и мир"


def test_repository_create_and_delete():
    repo = BookRepository()
    new_book = Book(0, "Тест", "Автор", 2024, "Тест", 500.0)
    created = repo.create(new_book)

    assert created.id == 5
    assert repo.get_by_id(5) is not None

    deleted = repo.delete(5)
    assert deleted is True
    assert repo.get_by_id(5) is None