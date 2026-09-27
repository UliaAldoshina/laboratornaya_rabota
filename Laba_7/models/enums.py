# models/enums.py
# Перечисление статусов книги

from enum import Enum


class BookStatus(Enum):  # Статусы книги
    AVAILABLE = "доступно"
    ISSUED = "выдано"
    RESERVED = "забронировано"