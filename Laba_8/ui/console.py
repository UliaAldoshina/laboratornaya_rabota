
# Пользовательский интерфейс

from factories.book_factory import ItemFactory
from strategies.standard_period import StandardPeriodStrategy
from strategies.preferential_period import PreferentialPeriodStrategy
from strategies.teacher_period import TeacherPeriodStrategy
from services.library_service import LibraryService


class ConsoleUI:  # Консольный интерфейс
    def __init__(self, service: LibraryService):
        self.service = service

    @staticmethod
    def input_int(prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Ошибка: введите целое число")

    @staticmethod
    def input_float(prompt: str) -> float:
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Ошибка: введите число")

    def choose_strategy(self):
        print("\nВыберите срок выдачи:")
        print("1. Стандартный (14 дней)")
        print("2. Льготный (30 дней)")
        print("3. Для преподавателей (60 дней)")
        choice = input("Выбор: ")
        if choice == "2":
            return PreferentialPeriodStrategy()
        if choice == "3":
            return TeacherPeriodStrategy()
        return StandardPeriodStrategy()

    def run(self) -> None:
        while True:
            print("\n" + "=" * 50)
            print("БИБЛИОТЕКА (паттерны проектирования)")
            print("=" * 50)
            print("1.  Показать все издания")
            print("2.  Добавить печатную книгу")
            print("3.  Добавить электронную книгу")
            print("4.  Добавить журнал")
            print("5.  Выдать издание")
            print("6.  Вернуть издание")
            print("7.  Забронировать издание")
            print("8.  Удалить издание")
            print("9.  Статистика")
            print("0.  Выход")
            print("=" * 50)

            choice = input("Выберите действие: ")

            if choice == "1":
                items = self.service.get_all()
                if not items:
                    print("Фонд пуст")
                else:
                    for i in items:
                        print(f"  {i.id}. {i.title} | {i.author} | "
                              f"{i.item_type.value} | {i.status.value}")

            elif choice == "2":
                title = input("Название: ")
                author = input("Автор: ")
                pages = self.input_int("Страниц: ")
                item = ItemFactory.create("printed", title, author, pages=pages)
                print(self.service.add_item(item))

            elif choice == "3":
                title = input("Название: ")
                author = input("Автор: ")
                size = self.input_float("Размер (МБ): ")
                item = ItemFactory.create("ebook", title, author, file_size=size)
                print(self.service.add_item(item))

            elif choice == "4":
                title = input("Название: ")
                author = input("Автор: ")
                issue = self.input_int("Номер выпуска: ")
                item = ItemFactory.create("magazine", title, author, issue_number=issue)
                print(self.service.add_item(item))

            elif choice == "5":
                item_id = self.input_int("ID издания: ")
                reader = input("Читатель: ")
                strategy = self.choose_strategy()
                print(self.service.issue(item_id, reader, strategy))

            elif choice == "6":
                item_id = self.input_int("ID издания: ")
                print(self.service.return_item(item_id))

            elif choice == "7":
                item_id = self.input_int("ID издания: ")
                reader = input("Читатель: ")
                print(self.service.reserve(item_id, reader))

            elif choice == "8":
                item_id = self.input_int("ID издания: ")
                print(self.service.delete_item(item_id))

            elif choice == "9":
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
                print("Ошибка: выберите пункт меню")