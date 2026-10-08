
# Интерфейс стратегии выдачи (Strategy)

from typing import Protocol


class IssuePeriodStrategy(Protocol):  # Стратегия срока выдачи
    def get_days(self) -> int:
        ...

    def get_name(self) -> str:
        ...