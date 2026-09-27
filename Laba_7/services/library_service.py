# services/library_service.py
# Бизнес-логика библиотеки

from datetime import date, timedelta
from models.entities import Book
from models.enums import BookStatus
from interfaces.repository import BookRepository
from interfaces.services import NotificationSender


class LibraryService:  # Сервис библиотеки
    def __init__(
        self,
        repository: BookRepository,     # DI через объединённый Protocol
        notifier: NotificationSender    # DI
    ):
        self.repository = repository
        self.notifier = notifier

    def add_book(self, book: Book) -> Book:  # Добавить книгу
        self.repository.add(book)
        return book

    def find_book(self, book_id: int) -> Book | None:  # Найти
        return self.repository.get(book_id)

    def issue_book(self, book_id: int, reader: str, days: int = 14) -> str:  # Выдать
        book = self.repository.get(book_id)
        if book is None:
            return "Книга не найдена"
        if book.status != BookStatus.AVAILABLE:
            return f"Нельзя выдать: статус '{book.status.value}'"

        book.status = BookStatus.ISSUED
        book.issued_to = reader
        book.due_date = date.today() + timedelta(days=days)
        self.repository.update(book)

        self.notifier.send(reader, f"Книга '{book.title}' выдана до {book.due_date}")
        return f"Выдано: '{book.title}' → {reader}"

    def return_book(self, book_id: int) -> str:  # Вернуть
        book = self.repository.get(book_id)
        if book is None:
            return "Книга не найдена"
        if book.status != BookStatus.ISSUED:
            return f"Нельзя вернуть: статус '{book.status.value}'"

        reader = book.issued_to
        book.status = BookStatus.AVAILABLE
        book.issued_to = None
        book.due_date = None
        self.repository.update(book)

        self.notifier.send(reader, f"Книга '{book.title}' возвращена")
        return f"Возвращено: '{book.title}'"

    def reserve_book(self, book_id: int, reader: str) -> str:  # Забронировать
        book = self.repository.get(book_id)
        if book is None:
            return "Книга не найдена"
        if book.status != BookStatus.AVAILABLE:
            return f"Нельзя забронировать: статус '{book.status.value}'"

        book.status = BookStatus.RESERVED
        book.issued_to = reader
        self.repository.update(book)

        self.notifier.send(reader, f"Книга '{book.title}' забронирована")
        return f"Забронировано: '{book.title}' → {reader}"

    def find_overdue(self) -> list[Book]:  # Просроченные
        today = date.today()
        return [b for b in self.repository.get_all()
                if b.status == BookStatus.ISSUED
                and b.due_date is not None
                and b.due_date < today]

    def get_statistics(self) -> dict:  # Статистика
        books = self.repository.get_all()
        statuses = [b.status for b in books]
        return {
            "total": len(books),
            "available": statuses.count(BookStatus.AVAILABLE),
            "issued": statuses.count(BookStatus.ISSUED),
            "reserved": statuses.count(BookStatus.RESERVED),
        }