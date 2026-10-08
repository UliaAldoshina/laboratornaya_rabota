
# Реализация репозитория в памяти

from models.entities import LibraryItem


class InMemoryRepository:  # Хранилище в памяти
    def __init__(self):
        self._items: dict[int, LibraryItem] = {}
        self._next_id = 1

    def add(self, item: LibraryItem) -> None:  # Добавить новое издание
        item.id = self._next_id
        self._items[item.id] = item
        self._next_id += 1

    def update(self, item: LibraryItem) -> None:  # Обновить без смены ID
        if item.id in self._items:
            self._items[item.id] = item

    def get(self, item_id: int) -> LibraryItem | None:
        return self._items.get(item_id)

    def get_all(self) -> list[LibraryItem]:
        return list(self._items.values())

    def delete(self, item_id: int) -> None:
        if item_id in self._items:
            del self._items[item_id]