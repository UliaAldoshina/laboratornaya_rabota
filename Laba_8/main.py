
# Точка входа

from repositories.memory_repository import InMemoryRepository
from services.library_service import LibraryService
from ui.console import ConsoleUI
from factories.book_factory import ItemFactory


def main() -> None:
    # Repository + DI
    repository = InMemoryRepository()
    service = LibraryService(repository)

    # Демонстрационные данные через Factory
    service.add_item(ItemFactory.create("printed", "Война и мир", "Толстой", pages=1300))
    service.add_item(ItemFactory.create("ebook", "Python", "Петров", file_size=15.5))
    service.add_item(ItemFactory.create("magazine", "Наука", "Редакция", issue_number=5))

    ConsoleUI(service).run()


if __name__ == "__main__":
    main()