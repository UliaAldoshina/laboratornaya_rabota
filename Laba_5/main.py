from models import Developer, Manager
from operations import (
    filter_objects,
    transform_objects,
    sort_objects,
    get_positions,
    find_highest_paid,
    has_department,
    all_salaries_positive,
    total_salary,
    average_salary,
    salary_dict
)
from generators import (
    employees_by_department,
    high_salary_employees,
    salary_generator,
    EmployeeIterator
)


def input_float(prompt):    #Безопасный ввод числа
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число")


def show_all(employees): #Вывод всех сотрудников
    if not employees:
        print("Список пуст")
        return
    for i, emp in enumerate(employees, 1):
        print(f"{i}. {emp}")


def main():    # Коллекция объектов (не менее 3 экземпляров)
    employees = [
        Developer("Иванов Иван", "IT", 85000, "Python", 3),
        Developer("Петров Пётр", "IT", 70000, "Java", 2),
        Manager("Сидорова Анна", "Продажи", 115000, 5),
        Manager("Козлов Дмитрий", "IT", 95000, 3),
        Developer("Смирнова Ольга", "Маркетинг", 65000, "JavaScript", 1),
    ]

    while True:
        print("\n" + "=" * 50)
        print("ФУНКЦИОНАЛЬНАЯ ОБРАБОТКА СОТРУДНИКОВ")
        print("=" * 50)
        print("1. Показать всех сотрудников")
        print("2. Фильтр по зарплате")
        print("3. Список должностей")
        print("4. Сортировка по зарплате")
        print("5. Самый высокооплачиваемый")
        print("6. Проверка наличия отдела")
        print("7. Сотрудники выбранного отдела")
        print("8. Зарплаты сотрудников")
        print("9. Статистика")
        print("0. Выход")
        print("=" * 50)

        choice = input("Выберите действие: ")

        if choice == "1":
            show_all(employees)

        elif choice == "2":
            min_s = input_float("Минимальная зарплата: ")
            max_s = input_float("Максимальная зарплата: ")
            result = filter_objects(
                employees,
                lambda e: min_s <= e.salary <= max_s
            )
            show_all(result)

        elif choice == "3":
            positions = get_positions(employees)
            print(f"\nУникальные должности ({len(positions)}):")
            for p in positions:
                print(f"  - {p}")

        elif choice == "4":
            order = input("По возрастанию (1) / убыванию (2)? ")
            reverse = (order == "2")
            # функция высшего порядка с lambda
            result = sort_objects(
                employees,
                key_function=lambda e: e.salary,
                reverse=reverse
            )
            show_all(result)

        elif choice == "5":
            best = find_highest_paid(employees)
            if best:
                print(f"\nСамый высокооплачиваемый:")
                print(f"  {best}")

        elif choice == "6":
            dept = input("Введите отдел: ")
            if has_department(employees, dept):
                print(f"Сотрудники отдела '{dept}' есть")
            else:
                print(f"Сотрудников отдела '{dept}' нет")

            if all_salaries_positive(employees):
                print("Все зарплаты положительные")
            else:
                print("Есть отрицательные зарплаты")

        elif choice == "7":
            dept = input("Введите отдел для генератора: ")
            print(f"\nСотрудники отдела '{dept}' (генератор):")
            found = False
            for emp in employees_by_department(employees, dept):
                print(f"  {emp}")
                found = True
            if not found:
                print("  Не найдено")

        elif choice == "8":
            print("\nЗарплаты:")
            for s in salary_generator(employees):
                print(f"  {s:.2f} руб.")

            print("\nВсе сотрудники:")
            for emp in EmployeeIterator(employees):
                print(f"  {emp.name}")

        elif choice == "9":
            print("\n" + "=" * 40)
            print("СТАТИСТИКА")
            print("=" * 40)
            print(f"Всего сотрудников: {len(employees)}")
            print(f"Общий фонд: {total_salary(employees):.2f} руб.")
            print(f"Средняя зарплата: {average_salary(employees):.2f} руб.")
            print("\nСловарь имя → зарплата:")
            for name, sal in salary_dict(employees).items():
                print(f"  {name}: {sal:.2f} руб.")

        elif choice == "0":
            print("Программа завершена")
            break

        else:
            print("Ошибка: выберите пункт из меню")


if __name__ == "__main__":
    main()