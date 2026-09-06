def input_emloyee(): #Ввод сотрудника
    name = input("Введите ФИО: ")
    post = input("Введите должность: ")
    department = input("Введите отдел: ")
    salary = float(input("Введите зарплату: "))
    return {"name": name, "post": post, "department": department, "salary": salary}

def print_emloyees(employees): #Вывод списка сотрудников
    print("\nСписок сотрудников")
    if not employees:
        print("Нет данных")
        return
    for emp in employees:
        print(f" {emp['name']} | {emp['post']} | {emp['department']} | {emp['salary']:.2f} руб.")

def find_by_department(employees, department): #Поиск сотрудников по отделу
    result = []
    for emp in employees:
        if emp["department"].lower() == department.lower():
            result.append(emp)
    return result

def filter_by_salary(employees, min_salary, max_salary): #Фильтрация по зарплате
    result = []
    for emp in employees:
        if min_salary <= emp["salary"] <= max_salary:
            result.append(emp)
    return result

def average_salary(employees): #Средняя зарплата
    total = 0
    for emp in employees:
        total += emp["salary"]
    return total / len(employees)

def find_highest_salary(employees): #Самый высокооплачиваемый сотрудник
    highest = employees[0]
    for emp in employees:
        if emp["salary"] > highest["salary"]:
            highest = emp
    return highest

def unique_post(employees): #Уникальность должности
    post = set()
    for emp in employees:
        post.add(emp["post"])
    return post

def sort_by_salary(employees): #Сортировка по зарплате
    return  sorted(employees, key=lambda  emp: emp["salary"], reverse=True)

def main():
    employees = []
    while True:
        print("\n" + "=" * 50)
        print("УПРАВЛЕНИЕ ДАННЫМИ СОТРУДНИКОВ")
        print("=" * 50)
        print("1. Ввести данные")
        print("2. Показать всех сотрудников")
        print("3. Поиск по отделу")
        print("4. Фильтрация по зарплате")
        print("5. Средняя зарплата")
        print("6. Самый высокооплачиваемый сотрудник")
        print("7. Уникальные должности")
        print("8. Сортировка по зарплате")
        print("9. Выход")
        print("=" * 50)
        choice = input("Выберите действие (1-9): ")
        if choice == "1":
            n = int(input("Введите количество сотрудников: "))
            for i in range(n):
                print(f"\nСотрудник {i + 1}:")
                emp = input_emloyee()
                employees.append(emp)
            print(f"Добавлено {n} сотрудников")

        elif choice == "2":
            print_emloyees(employees)

        elif choice == "3":
            if not employees:
                print("Ошибка! Сначала введите данные")
                continue
            department = input("Введите отдел для поиска: ")
            result = find_by_department(employees, department)
            if result:
                print_emloyees(result)
            else:
                print(f"Сотрудников в отделе '{department}' не найдено")

        elif choice == "4":
            if not employees:
                print("Ошибка! Сначала введите данные")
                continue
            min_s = float(input("Введите минимальную зарплату: "))
            max_s = float(input("Введите максимальную зарплату: "))
            result = filter_by_salary(employees, min_s, max_s)
            if result:
                print_emloyees(result)
            else:
                print("Сотрудников не найдено")

        elif choice == "5":
            if not employees:
                print("Ошибка! Сначала введите данные")
                continue
            average = average_salary(employees)
            print(f"\n Средняя зарплата: {average:.2f} руб.")

        elif choice == "6":
            if not employees:
                print("Ошибка! Сначала введите данные")
                continue
            highest = find_highest_salary(employees)
            print(f"\n Самый высокооплачиваемый сотрудник:")
            print(f" {highest['name']} | {highest['post']} | {highest['department']} | {highest['salary']:.2f} руб.")

        elif choice == "7":
            if not employees:
                print("Ошибка! Сначала введите данные")
                continue
            post = unique_post(employees)

            print(f"\nУникальные должности (всего {len(post)}):")
            for p in sorted(post):
                print(f" - {p}")

        elif choice == "8":
            if not employees:
                print("Ошибка! Сначала введите данные")
                continue
            print("\nСотрудники по убыванию зарплаты: ")
            sorted_employees = sort_by_salary(employees)
            print_emloyees(sorted_employees)

        elif choice == "9":
            print("Программа завершена")
            break

        else:
            print("Ошибка! Введите число от 1 до 9")

if __name__ == "__main__":
    main()