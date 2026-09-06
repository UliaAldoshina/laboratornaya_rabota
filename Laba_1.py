def average_salary(salary_list): #Средняя зарплата
    sum_salary = 0
    for s in salary_list:
        sum_salary += s
    return sum_salary / len(salary_list)

def max_min_salary(salary_list): #Максимальная и минимальная зарплата
    max_s = salary_list[0]
    min_s = salary_list[0]
    for s in salary_list:
        if s > max_s:
            max_s = s
        if s < min_s:
            min_s = s
    return max_s, min_s

def salary_more_then_average(salary_list, average): #Количество сотрудников с зарплатой выше средней
    employee_count = 0
    for s in salary_list:
        if s > average:
            employee_count += 1
    return employee_count

def salary_category(average): #Определение категории зарплаты
    if average < 25000:
        return "Низкая"
    elif average < 50000:
        return "Средняя"
    elif average < 75000:
        return  "Выше среднего"
    elif average < 100000:
        return "Высокая"
    return None


def main():
    salaries = []
    while True:
        print("\n" + "=" * 40)
        print("Анализ зарплаты сотрудников")
        print("=" * 40)
        print("1. Ввести данные")
        print("2. Показать статистику")
        print("3. Выход")
        print("=" * 40)
        choice = input("Выберите действие (1-3): ")
        if choice == "1":
            print("\nВвод данных о зарплатах")
            n = int(input("Введите количество сотрудников: "))
            for i in range(n):
                s = float(input(f"Введите зарплату сотрудника {i + 1}: "))
                salaries.append(s)
            print("Данные введены")
        elif choice == "2":
            if not salaries:
                print("Ошибка: сначала введите данные")
                continue
            average = average_salary(salaries)
            max_s, min_s = max_min_salary(salaries)
            more_than = salary_more_then_average(salaries, average)
            fund = sum(salaries)
            category = salary_category(average)

            print("\n" + "=" * 40)
            print("Результаты")
            print("=" * 40)
            print(f"Количество сотрудников: {n}")
            print(f"Средняя зарплата: {average:.2f} руб.")
            print(f"Максимальная зарплата: {max_s:.2f} руб.")
            print(f"Минимальная зарплата: {min_s:.2f} руб.")
            print(f"Сотрудников с заплатой выше среднего: {more_than}")
            print(f"Фонд заработной платы: {fund:.2f} руб.")
            print(f"Категория средней зарплаты: {category}")

            print("\nЗарплаты сотрудников:")
            for i in range(n):
                if salaries[i] > average:
                    print(f"Сотрудник {i + 1}: {salaries[i]:.2f} руб. (выше средней)")
                elif salaries[i] < average:
                    print(f"Сотрудник {i + 1}: {salaries[i]:.2f} руб. (ниже средней)")
                else:
                    print(f"Сотрудник {i + 1}: {salaries[i]:.2f} руб. (равна средней)")
        elif choice == "3":
            print("Программа завершена")
            break
        else:
            print("Ошибка! Введите 1, 2 или 3")
if __name__ == "__main__":
    main()