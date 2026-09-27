# protocols.py
# Protocol для отчётности

from typing import Protocol


class Reportable(Protocol):  # Протокол: объект умеет формировать отчёт

    def get_report_data(self) -> str:  # Метод отчёта
        ...