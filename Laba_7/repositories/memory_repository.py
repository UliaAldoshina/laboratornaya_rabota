# repositories/memory_repository.py
# Реализация репозитория в памяти

from models.entities import Book


class InMemoryBookRepository:  # Хранилище книг в памяти
    def __init__(self):
        self._books: dict[int, Book] = {}
        self._next_id: int = 1

    def add(self, book: Book) -> None:  # Добавить
        book.id = self._next_id
        self._books[book.id] = book
        self._next_id += 1

    def update(self, book: Book) -> None:  # Обновить
        self._books[book.id] = book

    def remove(self, book_id: int) -> None:  # Удалить
        if book_id in self._books:
            del self._books[book_id]

    def get(self, book_id: int) -> Book | None:  # Найти по ID
        return self._books.get(book_id)

    def get_all(self) -> list[Book]:  # Все книги
        return list(self._books.values())