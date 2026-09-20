from abc import ABC, abstractmethod

class Employee(ABC): #Базовый класс сотрудника

    def __init__(self, name, department, base_salary):
        self.name = name
        self.department = department
        self._base_salary = base_salary

    @property
    def base_salary(self): #Свойство для доступа к зарплате
        return self._base_salary

    @base_salary.setter
    def base_salary(self, value): #Сеттер с проверкой
        if value < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        self._base_salary = value

    @abstractmethod
    def calculate_salary(self):
        pass

    def get_info(self): #Общий метод получения информации
        return f"{self.name} | {self.department} | {self.calculate_salary():.2f} руб."

    def __str__(self):
        return self.get_info()

class Developer(Employee): #Класс разработчика

    def __init__(self, name, department, base_salary, language, projects_count):
        super().__init__(name, department, base_salary)
        self.language = language
        self.projects_count = projects_count

    def calculate_salary(self): #Зарплата разработчика: оклад + бонус за проекты
        bonus = self.projects_count * 5000
        return self._base_salary + bonus

    def get_info(self):
        return (f"{self.name} | {self.department} | Разработчик | "
                f"Язык: {self.language} | Проектов: {self.projects_count} | "
                f"Зарплата: {self.calculate_salary():.2f} руб.")


class Manager(Employee): #Класс менеджера
    def __init__(self, name, department, base_salary, subordinates_count, project_budget):
        super().__init__(name, department, base_salary)
        self.subordinates_count = subordinates_count
        self.project_budget = project_budget

    def calculate_salary(self): #Зарплата менеджера: оклад + бонус за подчинённых + % от бюджета
        bonus = self.subordinates_count * 3000
        budget_bonus = self.project_budget * 0.05
        return self._base_salary + bonus + budget_bonus

    def get_info(self):
        return (f"{self.name} | {self.department} | Менеджер | "
                f"Подчинённых: {self.subordinates_count} | "
                f"Бюджет: {self.project_budget:.2f} руб. | "
                f"Зарплата: {self.calculate_salary():.2f} руб.")


class Company: #Класс компании, содержащий сотрудников
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, employee): #Добавление сотрудника

        self.employees.append(employee)

    def show_all(self): #Показать всех сотрудников
        if not self.employees:
            print("Нет сотрудников")
            return
        print(f"\nСотрудники компании '{self.company_name}':")
        for i, emp in enumerate(self.employees, 1):
            print(f"{i}. {emp.get_info()}")

    def total_salary_fund(self): #Общий фонд зарплаты
        total = 0
        for emp in self.employees:
            total += emp.calculate_salary()
        return total

    def average_salary(self): #Средняя зарплата
        if not self.employees:
            return 0
        return self.total_salary_fund() / len(self.employees)

    def find_by_department(self, department): #Поиск сотрудников по отделу
        result = []
        for emp in self.employees:
            if emp.department.lower() == department.lower():
                result.append(emp)
        return result

    def find_highest_paid(self): #Самый высокооплачиваемый сотрудник
        if not self.employees:
            return None
        highest = self.employees[0]
        for emp in self.employees:
            if emp.calculate_salary() > highest.calculate_salary():
                highest = emp
        return highest

    def sort_by_salary(self): #Сортировка сотрудников по зарплате
        return sorted(self.employees, key=lambda emp: emp.calculate_salary())

    def unique_departments(self): #Уникальные отделы
        departments = set()
        for emp in self.employees:
            departments.add(emp.department)
        return departments

def main():
    company = Company("ООО Ромашка")

    company.add_employee(Developer("Иванов Иван", "IT", 70000, "Python", 3))
    company.add_employee(Developer("Петров Пётр", "IT", 60000, "Java", 2))
    company.add_employee(Manager("Сидорова Анна", "Продажи", 50000, 5, 1000000))
    company.add_employee(Manager("Козлов Дмитрий", "IT", 80000, 3, 500000))

    while True:
        print("\n" + "=" * 50)
        print(f"КОМПАНИЯ: {company.company_name}")
        print("=" * 50)
        print("1. Показать всех сотрудников")
        print("2. Поиск по отделу")
        print("3. Средняя зарплата")
        print("4. Самый высокооплачиваемый сотрудник")
        print("5. Уникальные отделы")
        print("6. Сортировка по зарплате")
        print("7. Фонд заработной платы")
        print("8. Выход")
        print("=" * 50)

        choice = input("Выберите действие (1-8): ")

        if choice == "1":
            company.show_all()

        elif choice == "2":
            department = input("Введите отдел для поиска: ")
            result = company.find_by_department(department)
            if result:
                print(f"\nСотрудники отдела '{department}':")
                for emp in result:
                    print(f"  {emp.get_info()}")
            else:
                print(f"Сотрудников в отделе '{department}' не найдено")

        elif choice == "3":
            avg = company.average_salary()
            print(f"\nСредняя зарплата: {avg:.2f} руб.")

        elif choice == "4":
            highest = company.find_highest_paid()
            if highest:
                print(f"\nСамый высокооплачиваемый сотрудник:")
                print(f"  {highest.get_info()}")

        elif choice == "5":
            departments = company.unique_departments()
            print(f"\nУникальные отделы (всего {len(departments)}):")
            for d in sorted(departments):
                print(f"  - {d}")

        elif choice == "6":
            sorted_emps = company.sort_by_salary()
            print("\nСотрудники по возрастанию зарплаты:")
            for i, emp in enumerate(sorted_emps, 1):
                print(f"{i}. {emp.get_info()}")

        elif choice == "7":
            fund = company.total_salary_fund()
            print(f"\nФонд заработной платы: {fund:.2f} руб.")

        elif choice == "8":
            print("Программа завершена")
            break

        else:
            print("Ошибка! Введите число от 1 до 8")


if __name__ == "__main__":
    main()