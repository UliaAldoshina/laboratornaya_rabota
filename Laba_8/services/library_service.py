
# Бизнес-логика

from interfaces.repository import Repository
from commands.book_commands import IssueCommand, ReturnCommand, ReserveCommand


class LibraryService:  # Сервис библиотеки
    def __init__(self, repository: Repository):
        self.repository = repository

    def add_item(self, item) -> str:
        self.repository.add(item)
        return f"Добавлено: {item.title}"

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, item_id: int):
        return self.repository.get(item_id)

    def delete_item(self, item_id: int) -> str:
        item = self.repository.get(item_id)
        if item is None:
            return "Издание не найдено"
        self.repository.delete(item_id)
        return f"Удалено: {item.title}"

    # Вызов команд (Command pattern)
    def issue(self, item_id: int, reader: str, strategy) -> str:
        return IssueCommand(self.repository, item_id, reader, strategy).execute()

    def return_item(self, item_id: int) -> str:
        return ReturnCommand(self.repository, item_id).execute()

    def reserve(self, item_id: int, reader: str) -> str:
        return ReserveCommand(self.repository, item_id, reader).execute()

    def get_statistics(self) -> dict:
        items = self.repository.get_all()
        return {
            "total": len(items),
            "available": sum(1 for i in items if i.status.value == "доступно"),
            "issued": sum(1 for i in items if i.status.value == "выдано"),
            "reserved": sum(1 for i in items if i.status.value == "забронировано"),
        }