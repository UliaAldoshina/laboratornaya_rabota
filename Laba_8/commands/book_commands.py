
# Command: команды выдачи, возврата, бронирования

from datetime import date, timedelta
from models.enums import BookStatus


class IssueCommand:  # Команда: выдать
    def __init__(self, repository, item_id: int, reader: str, strategy):
        self.repository = repository
        self.item_id = item_id
        self.reader = reader
        self.strategy = strategy

    def execute(self) -> str:
        item = self.repository.get(self.item_id)
        if item is None:
            return "Издание не найдено"
        if item.status != BookStatus.AVAILABLE:
            return f"Нельзя выдать: статус '{item.status.value}'"

        days = self.strategy.get_days()
        item.status = BookStatus.ISSUED
        item.issued_to = self.reader
        item.due_date = date.today() + timedelta(days=days)
        self.repository.update(item)  # Обновляем, не создаём заново
        return (f"Выдано: '{item.title}' -> {self.reader} "
                f"({self.strategy.get_name()})")


class ReturnCommand:  # Команда: вернуть
    def __init__(self, repository, item_id: int):
        self.repository = repository
        self.item_id = item_id

    def execute(self) -> str:
        item = self.repository.get(self.item_id)
        if item is None:
            return "Издание не найдено"
        if item.status != BookStatus.ISSUED:
            return f"Нельзя вернуть: статус '{item.status.value}'"

        item.status = BookStatus.AVAILABLE
        item.issued_to = None
        item.due_date = None
        self.repository.update(item)  # Обновляем, не создаём заново
        return f"Возвращено: '{item.title}'"


class ReserveCommand:  # Команда: забронировать
    def __init__(self, repository, item_id: int, reader: str):
        self.repository = repository
        self.item_id = item_id
        self.reader = reader

    def execute(self) -> str:
        item = self.repository.get(self.item_id)
        if item is None:
            return "Издание не найдено"
        if item.status != BookStatus.AVAILABLE:
            return f"Нельзя забронировать: статус '{item.status.value}'"

        item.status = BookStatus.RESERVED
        item.issued_to = self.reader
        self.repository.update(item)  # Обновляем, не создаём заново
        return f"Забронировано: '{item.title}' для {self.reader}"