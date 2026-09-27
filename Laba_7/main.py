# main.py
# Точка входа: собираем зависимости (Dependency Injection)

from repositories.memory_repository import InMemoryBookRepository
from infrastructure.notifier import EmailSender, SmsSender
from services.library_service import LibraryService
from ui.console import ConsoleUI
from models.entities import PrintedBook, EBook


def main() -> None:
    # 1. Создаём зависимости
    repository = InMemoryBookRepository()      # DIP: абстракция репозитория
    notifier = EmailSender()                   # можно заменить на SmsSender

    # 2. Внедряем зависимости в сервис (Constructor Injection)
    service = LibraryService(repository, notifier)

    # 3. Демонстрационные данные
    service.add_book(PrintedBook(
        id=0, title="Война и мир", author="Толстой Л.Н.",
        pages=1300, publisher="АСТ"
    ))
    service.add_book(EBook(
        id=0, title="Python для всех", author="Петров П.",
        file_size=15.5, file_format="PDF"
    ))

    # 4. Запускаем UI
    ui = ConsoleUI(service)
    ui.run()


if __name__ == "__main__":
    main()