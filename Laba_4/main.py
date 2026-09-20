from storage import Storage
from services import EmployeeService


def input_int(prompt): #Безопасный ввод целого числа
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число")


def input_float(prompt):  #Безопасный ввод дробного числа
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число")


def main():
    storage = Storage("employees.json")
    service = EmployeeService(storage)

    while True:
        print("\n" + "=" * 50)
        print("СИСТЕМА УЧЁТА СОТРУДНИКОВ")
        print("=" * 50)
        print("1. Показать всех сотрудников")
        print("2. Добавить сотрудника")
        print("3. Найти по ФИО")
        print("4. Найти по отделу")
        print("5. Изменить зарплату")
        print("6. Удалить сотрудника")
        print("7. Статистика зарплат")
        print("8. Сохранить в файл")
        print("9. Выход")
        print("=" * 50)

        choice = input("Выберите действие (1-9): ")

        if choice == "1":
            service.show_all()

        elif choice == "2":
            name = input("Введите ФИО: ")
            position = input("Введите должность: ")
            department = input("Введите отдел: ")
            salary = input_float("Введите зарплату: ")
            service.add_employee(name, position, department, salary)

        elif choice == "3":
            name = input("Введите ФИО для поиска: ")
            try:
                emp = service.find_by_name(name)
                print(f"Найден: {emp}")
            except Exception as error:
                print(f"Ошибка: {error}")

        elif choice == "4":
            department = input("Введите отдел: ")
            result = service.find_by_department(department)
            if result:
                print(f"\nСотрудники отдела '{department}':")
                for emp in result:
                    print(f"  {emp}")
            else:
                print(f"Сотрудников в отделе '{department}' не найдено")

        elif choice == "5":
            name = input("Введите ФИО: ")
            new_salary = input_float("Введите новую зарплату: ")
            service.change_salary(name, new_salary)

        elif choice == "6":
            name = input("Введите ФИО для удаления: ")
            service.delete_employee(name)

        elif choice == "7":
            stats = service.get_statistics()
            if stats is None:
                print("Нет данных для статистики")
            else:
                print("\n" + "=" * 40)
                print("СТАТИСТИКА ЗАРПЛАТ")
                print("=" * 40)
                print(f"Количество сотрудников: {stats['count']}")
                print(f"Общий фонд: {stats['total']:.2f} руб.")
                print(f"Средняя зарплата: {stats['average']:.2f} руб.")
                print(f"Максимальная: {stats['max']:.2f} руб.")
                print(f"Минимальная: {stats['min']:.2f} руб.")

        elif choice == "8":
            service.storage.save(service.employees)

        elif choice == "9":
            service.storage.save(service.employees)
            print("Данные сохранены. Программа завершена")
            break

        else:
            print("Ошибка: выберите число от 1 до 9")


if __name__ == "__main__":
    main()