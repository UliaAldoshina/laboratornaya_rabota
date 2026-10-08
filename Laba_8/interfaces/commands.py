
# Интерфейс команды (Command)

from typing import Protocol


class Command(Protocol):  # Интерфейс команды
    def execute(self) -> str:
        ...