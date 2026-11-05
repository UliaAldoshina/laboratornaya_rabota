import pytest
from repository.book_repository import BookRepository
import sqlite3


@pytest.fixture
def repo(tmp_path):
    # Создаем уникальный временный файл базы данных для каждого теста
    db_file = tmp_path / "test.db"

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT);")
    cursor.execute("""
        CREATE TABLE books (
            id INTEGER PRIMARY KEY, 
            title TEXT, 
            author_id INTEGER, 
            year INTEGER, 
            price REAL, 
            is_available BOOLEAN,
            FOREIGN KEY(author_id) REFERENCES authors(id)
        );
    """)
    cursor.execute("INSERT INTO authors (id, name) VALUES (1, 'Тестовый Автор');")
    cursor.execute(
        "INSERT INTO books (id, title, author_id, year, price, is_available) VALUES (1, 'Тест Книга', 1, 2022, 500.0, 1);")
    conn.commit()
    conn.close()

    repository = BookRepository(str(db_file))
    return repository


def test_repo_get_all(repo):
    books = repo.get_all()
    assert len(books) == 1
    assert books[0]["title"] == "Тест Книга"


def test_repo_get_by_id(repo):
    book = repo.get_by_id(1)
    assert book is not None
    assert book["author"] == "Тестовый Автор"


def test_repo_delete(repo):
    success = repo.delete(1)
    assert success is True
    assert repo.get_by_id(1) is None