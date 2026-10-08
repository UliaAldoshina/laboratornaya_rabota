
# Интерфейс репозитория (Repository)

from typing import Protocol
from models.entities import LibraryItem


class Repository(Protocol):  # Интерфейс хранилища
    def add(self, item: LibraryItem) -> None:
        ...

    def update(self, item: LibraryItem) -> None:  # Обновление без смены ID
        ...

    def get(self, item_id: int) -> LibraryItem | None:
        ...

    def get_all(self) -> list[LibraryItem]:
        ...

    def delete(self, item_id: int) -> None:
        ...