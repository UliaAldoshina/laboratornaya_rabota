# models/entities.py
# Модели предметной области

from dataclasses import dataclass
from datetime import date
from models.enums import BookStatus


@dataclass
class Book:  # Книга — базовый класс
    id: int
    title: str
    author: str
    status: BookStatus = BookStatus.AVAILABLE
    issued_to: str | None = None
    due_date: date | None = None

    def get_report_data(self) -> str:
        return (f"ID: {self.id} | {self.title} | {self.author} | "
                f"{self.status.value}")


@dataclass
class PrintedBook(Book):  # Печатная книга
    pages: int = 0
    publisher: str = ""

    def get_report_data(self) -> str:
        return (f"[ПЕЧАТНАЯ] ID: {self.id} | {self.title} | {self.author} | "
                f"{self.pages} стр. | {self.publisher} | {self.status.value}")


@dataclass
class EBook(Book):  # Электронная книга
    file_size: float = 0.0
    file_format: str = "PDF"

    def get_report_data(self) -> str:
        return (f"[ЭЛЕКТРОННАЯ] ID: {self.id} | {self.title} | {self.author} | "
                f"{self.file_size} МБ | {self.file_format} | {self.status.value}")