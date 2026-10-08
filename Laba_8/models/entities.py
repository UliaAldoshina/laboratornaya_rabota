
# Модели предметной области (dataclass)

from dataclasses import dataclass
from datetime import date
from models.enums import BookStatus, ItemType


@dataclass
class LibraryItem:  # Базовый класс издания
    id: int
    title: str
    author: str
    item_type: ItemType
    status: BookStatus = BookStatus.AVAILABLE
    issued_to: str | None = None
    due_date: date | None = None


@dataclass
class PrintedBook(LibraryItem):  # Печатная книга
    pages: int = 0

    def __post_init__(self):
        self.item_type = ItemType.PRINTED


@dataclass
class EBook(LibraryItem):  # Электронная книга
    file_size: float = 0.0

    def __post_init__(self):
        self.item_type = ItemType.EBOOK


@dataclass
class Magazine(LibraryItem):  # Журнал
    issue_number: int = 0

    def __post_init__(self):
        self.item_type = ItemType.MAGAZINE