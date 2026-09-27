# ui/console.py
# Пользовательский интерфейс (отделён от бизнес-логики)

from models.entities import PrintedBook, EBook
from services.library_service import LibraryService


class ConsoleUI:  # Консольный интерфейс
    def __init__(self, service: LibraryService):  # DI
        self.service = service

    @staticmethod
    def input_int(prompt: str) -> int:  # Безопасный int
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Ошибка: введите целое число")

    @staticmethod
    def input_float(prompt: str) -> float:  # Безопасный float
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Ошибка: введите число")

    def run(self) -> None:  # Главное меню
        while True:
            print("\n" + "=" * 50)
            print("БИБЛИОТЕКА")
            print("=" * 50)
            print("1. Показать все книги")
            print("2. Добавить печатную книгу")
            print("3. Добавить электронную книгу")
            print("4. Выдать книгу")
            print("5. Вернуть книгу")
            print("6. Забронировать книгу")
            print("7. Просроченные выдачи")
            print("8. Статистика")
            print("0. Выход")
            print("=" * 50)

            choice = input("Выберите действие: ")

            if choice == "1":
                books = self.service.repository.get_all()
                if not books:
                    print("Фонд пуст")
                else:
                    for b in books:
                        print(f"  {b.get_report_data()}")

            elif choice == "2":
                title = input("Название: ")
                author = input("Автор: ")
                pages = self.input_int("Страниц: ")
                publisher = input("Издательство: ")
                book = PrintedBook(id=0, title=title, author=author,
                                   pages=pages, publisher=publisher)
                self.service.add_book(book)
                print(f"Добавлено: {book.title}")

            elif choice == "3":
                title = input("Название: ")
                author = input("Автор: ")
                size = self.input_float("Размер (МБ): ")
                fmt = input("Формат: ")
                book = EBook(id=0, title=title, author=author,
                             file_size=size, file_format=fmt)
                self.service.add_book(book)
                print(f"Добавлено: {book.title}")

            elif choice == "4":
                bid = self.input_int("ID книги: ")
                reader = input("Читатель: ")
                days = self.input_int("На сколько дней: ")
                print(self.service.issue_book(bid, reader, days))

            elif choice == "5":
                bid = self.input_int("ID книги: ")
                print(self.service.return_book(bid))

            elif choice == "6":
                bid = self.input_int("ID книги: ")
                reader = input("Читатель: ")
                print(self.service.reserve_book(bid, reader))

            elif choice == "7":
                overdue = self.service.find_overdue()
                if overdue:
                    print(f"\nПросроченные ({len(overdue)}):")
                    for b in overdue:
                        print(f"  {b.title} — {b.issued_to} (до {b.due_date})")
                else:
                    print("Просроченных нет")

            elif choice == "8":
                stats = self.service.get_statistics()
                print("\n" + "=" * 40)
                print("СТАТИСТИКА")
                print("=" * 40)
                print(f"Всего: {stats['total']}")
                print(f"Доступно: {stats['available']}")
                print(f"Выдано: {stats['issued']}")
                print(f"Забронировано: {stats['reserved']}")

            elif choice == "0":
                print("Работа завершена")
                break

            else:
                print("Ошибка: выберите пункт из меню")