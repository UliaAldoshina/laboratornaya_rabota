
# Перечисления

from enum import Enum


class ItemType(Enum):  # Тип издания
    PRINTED = "печатная книга"
    EBOOK = "электронная книга"
    MAGAZINE = "журнал"


class BookStatus(Enum):  # Статус издания
    AVAILABLE = "доступно"
    ISSUED = "выдано"
    RESERVED = "забронировано"


class ReaderType(Enum):  # Тип читателя
    STUDENT = "студент"
    PREFERENTIAL = "льготник"
    TEACHER = "преподаватель"