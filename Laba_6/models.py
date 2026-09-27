# models.py
# Классы данных (dataclass) и перечисления (Enum)

from dataclasses import dataclass
from enum import Enum
from datetime import date


class Status(Enum):  # Статусы изданий
    AVAILABLE = "доступно"
    ISSUED = "выдано"
    RESERVED = "зарезервировано"


@dataclass
class Entity:  # Базовый класс издания
    id: int
    title: str
    author: str
    year: int
    status: Status = Status.AVAILABLE
    issued_to: str | None = None
    due_date: date | None = None

    def get_report_data(self) -> str:  # Отчёт по изданию
        return (f"ID: {self.id} | {self.title} | {self.author} | "
                f"{self.year} | Статус: {self.status.value}")


@dataclass
class Book(Entity):  # Книга
    pages: int = 0
    genre: str = ""

    def get_report_data(self) -> str:  # Отчёт по книге
        return (f"[КНИГА] ID: {self.id} | {self.title} | {self.author} | "
                f"{self.year} | {self.pages} стр. | Жанр: {self.genre} | "
                f"Статус: {self.status.value}")


@dataclass
class Magazine(Entity):  # Журнал
    issue_number: int = 0
    periodicity: str = ""

    def get_report_data(self) -> str:  # Отчёт по журналу
        return (f"[ЖУРНАЛ] ID: {self.id} | {self.title} | {self.author} | "
                f"{self.year} | Выпуск №{self.issue_number} | "
                f"{self.periodicity} | Статус: {self.status.value}")


@dataclass
class EPublication(Entity):  # Электронное издание
    file_size: float = 0.0
    format: str = "PDF"

    def get_report_data(self) -> str:  # Отчёт по эл. изданию
        return (f"[ЭЛ. ИЗДАНИЕ] ID: {self.id} | {self.title} | {self.author} | "
                f"{self.year} | {self.file_size} МБ | {self.format} | "
                f"Статус: {self.status.value}")