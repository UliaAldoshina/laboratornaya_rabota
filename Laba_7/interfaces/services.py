# interfaces/services.py
# Интерфейсы сервисов (DIP)

from typing import Protocol


class NotificationSender(Protocol):  # Интерфейс: уведомления
    def send(self, recipient: str, message: str) -> None:
        ...


class Reportable(Protocol):  # Интерфейс: отчёт
    def get_report_data(self) -> str:
        ...