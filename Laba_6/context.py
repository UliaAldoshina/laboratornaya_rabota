# context.py
# Контекстные менеджеры

import time
from contextlib import contextmanager


class OperationLogger:  # Контекстный менеджер: журнал операции

    def __init__(self, operation_name: str):  # Конструктор
        self.operation_name = operation_name

    def __enter__(self):  # Вход в блок with
        print(f"\n>>> НАЧАЛО: {self.operation_name}")
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):  # Выход
        elapsed = time.perf_counter() - self.start
        if exc_type is not None:
            print(f"<<< ОШИБКА: {exc_value}")
        else:
            print(f"<<< ЗАВЕРШЕНО ({elapsed:.4f} сек)")
        return False


@contextmanager
def temporary_status(entity, new_status):  # Временное изменение статуса
    old_status = entity.status
    entity.status = new_status
    print(f"[CTX] Статус '{entity.title}' → '{new_status.value}'")
    try:
        yield entity
    finally:
        entity.status = old_status
        print(f"[CTX] Статус '{entity.title}' ← '{old_status.value}'")