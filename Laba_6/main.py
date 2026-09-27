# main.py
# Меню и запуск

from models import Status
from services import LibraryService, print_report
from context import OperationLogger, temporary_status
from decorators import repeat
from introspection import inspect_object
from exceptions import EntityNotFoundError, InvalidStatusError


def input_int(prompt: str) -> int:  # Безопасный ввод целого
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число")


def input_float(prompt: str) -> float:  # Безопасный ввод дробного
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число")


def demo_decorators() -> None:  # Демонстрация декоратора @repeat
    print("\n--- Демонстрация декоратора @repeat(3) ---")

    @repeat(3)
    def hello() -> None:  # Функция для демонстрации
        print("Привет из библиотеки!")

    hello()


def demo_context(service: LibraryService) -> None:  # Демонстрация контекста
    print("\n--- Демонстрация контекстного менеджера ---")
    with OperationLogger("Подсчёт фонда"):
        print(f"  Всего изданий: {len(service.entities)}")

    if service.entities:
        entity = service.entities[0]
        print(f"\nВременное изменение статуса '{entity.title}':")
        with temporary_status(entity, Status.RESERVED):
            print(f"  Внутри блока: {entity.status.value}")
        print(f"  После блока: {entity.status.value}")


def demo_protocol(service: LibraryService) -> None:  # Демонстрация Protocol
    print("\n--- Демонстрация Protocol ---")
    if not service.entities:
        print("  Нет изданий")
        return
    for entity in service.entities[:3]:
        print_report(entity)


def main() -> None:  # Главная функция
    service = LibraryService()

    while True:
        print("\n" + "=" * 50)
        print("БИБЛИОТЕКА")
        print("=" * 50)
        print("1.  Показать все издания")
        print("2.  Добавить книгу")
        print("3.  Добавить журнал")
        print("4.  Добавить электронное издание")
        print("5.  Найти по названию")
        print("6.  Удалить издание")
        print("7.  Выдать издание")
        print("8.  Вернуть издание")
        print("9.  Зарезервировать издание")
        print("10. Просроченные выдачи")
        print("11. Статистика фонда")
        print("12. Интроспекция объекта")
        print("13. Демонстрация декоратора")
        print("14. Демонстрация контекстного менеджера")
        print("15. Демонстрация Protocol")
        print("0.  Выход")
        print("=" * 50)

        choice = input("Выберите действие: ")

        try:
            if choice == "1":  # Показать все
                if not service.entities:
                    print("Фонд пуст")
                else:
                    print("\nИздания в фонде:")
                    for e in service.entities:
                        print(f"  {e.get_report_data()}")

            elif choice == "2":  # Добавить книгу
                title = input("Название: ")
                author = input("Автор: ")
                year = input_int("Год: ")
                pages = input_int("Страниц: ")
                genre = input("Жанр: ")
                book = service.add_book(title, author, year, pages, genre)
                print(f"Добавлено: {book.title}")

            elif choice == "3":  # Добавить журнал
                title = input("Название: ")
                author = input("Автор: ")
                year = input_int("Год: ")
                issue = input_int("Номер выпуска: ")
                periodicity = input("Периодичность: ")
                mag = service.add_magazine(title, author, year, issue, periodicity)
                print(f"Добавлено: {mag.title}")

            elif choice == "4":  # Добавить эл. издание
                title = input("Название: ")
                author = input("Автор: ")
                year = input_int("Год: ")
                size = input_float("Размер (МБ): ")
                fmt = input("Формат: ")
                ep = service.add_epublication(title, author, year, size, fmt)
                print(f"Добавлено: {ep.title}")

            elif choice == "5":  # Найти
                title = input("Введите часть названия: ")
                found = service.find_by_title(title)
                if found:
                    print("\nНайдено:")
                    for e in found:
                        print(f"  {e.get_report_data()}")
                else:
                    print("Ничего не найдено")

            elif choice == "6":  # Удалить
                eid = input_int("ID издания: ")
                print(service.delete_entity(eid))

            elif choice == "7":  # Выдать
                eid = input_int("ID издания: ")
                reader = input("ФИО читателя: ")
                days = input_int("На сколько дней: ")
                print(service.issue_entity(eid, reader, days))

            elif choice == "8":  # Вернуть
                eid = input_int("ID издания: ")
                print(service.return_entity(eid))

            elif choice == "9":  # Зарезервировать
                eid = input_int("ID издания: ")
                reader = input("ФИО читателя: ")
                print(service.reserve_entity(eid, reader))

            elif choice == "10":  # Просроченные
                overdue = service.find_overdue()
                if overdue:
                    print(f"\nПросроченные выдачи ({len(overdue)}):")
                    for e in overdue:
                        print(f"  {e.title} — {e.issued_to} (срок: {e.due_date})")
                else:
                    print("Просроченных выдач нет")

            elif choice == "11":  # Статистика
                stats = service.get_statistics()
                if stats:
                    print("\n" + "=" * 40)
                    print("СТАТИСТИКА ФОНДА")
                    print("=" * 40)
                    print(f"Всего изданий: {stats['total']}")
                    print(f"  Книг: {stats['books']}")
                    print(f"  Журналов: {stats['magazines']}")
                    print(f"  Электронных: {stats['epublications']}")
                    print(f"Доступно: {stats['available']}")
                    print(f"Выдано: {stats['issued']}")
                    print(f"Зарезервировано: {stats['reserved']}")
                else:
                    print("Нет данных")

            elif choice == "12":  # Интроспекция
                eid = input_int("ID издания: ")
                try:
                    entity = service.find_by_id(eid)
                    inspect_object(entity)
                except EntityNotFoundError as e:
                    print(f"Ошибка: {e}")

            elif choice == "13":  # Декоратор
                demo_decorators()

            elif choice == "14":  # Контекст
                demo_context(service)

            elif choice == "15":  # Protocol
                demo_protocol(service)

            elif choice == "0":  # Выход
                print("Работа завершена")
                break

            else:
                print("Ошибка: выберите пункт из меню")

        except EntityNotFoundError as e:  # Издание не найдено
            print(f"Ошибка: {e}")
        except InvalidStatusError as e:  # Неверный статус
            print(f"Ошибка статуса: {e}")
        except ValueError as e:  # Неверное значение
            print(f"Ошибка значения: {e}")
        except Exception as e:  # Прочие ошибки
            print(f"Непредвиденная ошибка: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()