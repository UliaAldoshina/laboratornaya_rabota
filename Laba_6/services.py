# services.py
# Бизнес-логика

from datetime import date, timedelta
from models import Entity, Status, Book, Magazine, EPublication
from exceptions import EntityNotFoundError, InvalidStatusError
from decorators import log_call, measure_time
from protocols import Reportable


class LibraryService:  # Сервис управления библиотекой

    def __init__(self):  # Конструктор
        self.entities: list[Entity] = []
        self._next_id = 1

    def _generate_id(self) -> int:  # Сгенерировать ID
        current = self._next_id
        self._next_id += 1
        return current

    @log_call
    def add_book(self, title: str, author: str, year: int,
                 pages: int, genre: str) -> Book:  # Добавить книгу
        book = Book(
            id=self._generate_id(),
            title=title, author=author, year=year,
            pages=pages, genre=genre
        )
        self.entities.append(book)
        return book

    @log_call
    def add_magazine(self, title: str, author: str, year: int,
                     issue_number: int, periodicity: str) -> Magazine:  # Добавить журнал
        mag = Magazine(
            id=self._generate_id(),
            title=title, author=author, year=year,
            issue_number=issue_number, periodicity=periodicity
        )
        self.entities.append(mag)
        return mag

    @log_call
    def add_epublication(self, title: str, author: str, year: int,
                         file_size: float, fmt: str) -> EPublication:  # Добавить эл. издание
        ep = EPublication(
            id=self._generate_id(),
            title=title, author=author, year=year,
            file_size=file_size, format=fmt
        )
        self.entities.append(ep)
        return ep

    def find_by_id(self, entity_id: int) -> Entity:  # Найти по ID
        for e in self.entities:
            if e.id == entity_id:
                return e
        raise EntityNotFoundError(f"Издание с ID={entity_id} не найдено")

    def find_by_title(self, title: str) -> list[Entity]:  # Найти по названию
        return [e for e in self.entities
                if title.lower() in e.title.lower()]

    @log_call
    def delete_entity(self, entity_id: int) -> str:  # Удалить издание
        entity = self.find_by_id(entity_id)
        self.entities.remove(entity)
        return f"Удалено: {entity.title}"

    @log_call
    def issue_entity(self, entity_id: int, reader: str, days: int = 14) -> str:  # Выдать
        entity = self.find_by_id(entity_id)
        if entity.status != Status.AVAILABLE:
            raise InvalidStatusError(
                f"Нельзя выдать: статус '{entity.status.value}'"
            )
        entity.status = Status.ISSUED
        entity.issued_to = reader
        entity.due_date = date.today() + timedelta(days=days)
        return f"Выдано: '{entity.title}' → {reader} до {entity.due_date}"

    @log_call
    def return_entity(self, entity_id: int) -> str:  # Вернуть
        entity = self.find_by_id(entity_id)
        if entity.status != Status.ISSUED:
            raise InvalidStatusError(
                f"Нельзя вернуть: статус '{entity.status.value}'"
            )
        entity.status = Status.AVAILABLE
        reader = entity.issued_to
        entity.issued_to = None
        entity.due_date = None
        return f"Возвращено: '{entity.title}' от {reader}"

    @log_call
    def reserve_entity(self, entity_id: int, reader: str) -> str:  # Зарезервировать
        entity = self.find_by_id(entity_id)
        if entity.status != Status.AVAILABLE:
            raise InvalidStatusError(
                f"Нельзя зарезервировать: статус '{entity.status.value}'"
            )
        entity.status = Status.RESERVED
        entity.issued_to = reader
        return f"Зарезервировано: '{entity.title}' для {reader}"

    def find_overdue(self) -> list[Entity]:  # Просроченные выдачи
        today = date.today()
        return [e for e in self.entities
                if e.status == Status.ISSUED
                and e.due_date is not None
                and e.due_date < today]

    @measure_time
    def get_statistics(self) -> dict:  # Статистика
        if not self.entities:
            return {}
        statuses = [e.status for e in self.entities]
        return {
            "total": len(self.entities),
            "books": sum(1 for e in self.entities if isinstance(e, Book)),
            "magazines": sum(1 for e in self.entities if isinstance(e, Magazine)),
            "epublications": sum(1 for e in self.entities if isinstance(e, EPublication)),
            "available": statuses.count(Status.AVAILABLE),
            "issued": statuses.count(Status.ISSUED),
            "reserved": statuses.count(Status.RESERVED),
        }


def print_report(reportable: Reportable) -> None:  # Печать через Protocol
    print(reportable.get_report_data())