# interfaces/repository.py
# Интерфейсы репозитория

from typing import Protocol
from models.entities import Book


class ReadableRepository(Protocol):  # Интерфейс: только чтение
    def get(self, book_id: int) -> Book | None:
        ...

    def get_all(self) -> list[Book]:
        ...


class WritableRepository(Protocol):  # Интерфейс: только запись
    def add(self, book: Book) -> None:
        ...

    def update(self, book: Book) -> None:
        ...

    def remove(self, book_id: int) -> None:
        ...


class BookRepository(ReadableRepository, WritableRepository, Protocol):
    """Объединённый интерфейс: чтение + запись"""
    pass