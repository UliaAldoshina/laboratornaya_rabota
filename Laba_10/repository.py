from typing import List, Optional
from models import Book


class BookRepository:
    def __init__(self):
        self._storage: dict[int, Book] = {}
        self._counter: int = 1
        self._seed_data()

    def _seed_data(self):
        initial_books = [
            Book(1, "Война и мир", "Лев Толстой", 1869, "Роман", 1200.0, True),
            Book(2, "Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 850.0, True),
            Book(3, "Мастер и Маргарита", "Михаил Булгаков", 1967, "Фантастика", 950.0, False),
            Book(4, "Анна Каренина", "Лев Толстой", 1877, "Роман", 900.0, True),
        ]
        for book in initial_books:
            self._storage[book.id] = book
        self._counter = 5

    def get_all(self) -> List[Book]:
        return list(self._storage.values())

    def get_by_id(self, book_id: int) -> Optional[Book]:
        return self._storage.get(book_id)

    def create(self, book: Book) -> Book:
        book.id = self._counter
        self._storage[book.id] = book
        self._counter += 1
        return book

    def update(self, book: Book) -> Book:
        self._storage[book.id] = book
        return book

    def delete(self, book_id: int) -> bool:
        if book_id in self._storage:
            del self._storage[book_id]
            return True
        return False