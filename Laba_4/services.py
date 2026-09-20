from exceptions import EmployeeNotFoundError, NegativeSalaryError


class EmployeeService:#Сервис для работы с сотрудниками

    def __init__(self, storage):
        self.storage = storage
        self.employees = storage.load()

    def add_employee(self, name, position, department, salary):    #Добавить сотрудника
        from models import Employee
        try:
            employee = Employee(name, position, department, salary)
            self.employees.append(employee)
            self.storage.save(self.employees)
            return employee
        except NegativeSalaryError as error:
            print(f"Ошибка: {error}")
            return None

    def find_by_name(self, name):    #Найти сотрудника по ФИО
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                return emp
        raise EmployeeNotFoundError(f"Сотрудник '{name}' не найден")

    def find_by_department(self, department):  #Найти сотрудников по отделу
        result = []
        for emp in self.employees:
            if emp.department.lower() == department.lower():
                result.append(emp)
        return result

    def change_salary(self, name, new_salary):    #Изменить зарплату сотрудника
        try:
            employee = self.find_by_name(name)
            employee.salary = new_salary
            self.storage.save(self.employees)
            print(f"Зарплата сотрудника {employee.name} изменена на {new_salary:.2f} руб.")
        except NegativeSalaryError as error:
            print(f"Ошибка: {error}")
        except EmployeeNotFoundError as error:
            print(f"Ошибка: {error}")

    def delete_employee(self, name):   #Удалить сотрудника
        try:
            employee = self.find_by_name(name)
            self.employees.remove(employee)
            self.storage.save(self.employees)
            print(f"Сотрудник {employee.name} удалён")
        except EmployeeNotFoundError as error:
            print(f"Ошибка: {error}")

    def get_statistics(self):   #Статистика по зарплатам
        if not self.employees:
            return None
        salaries = [emp.salary for emp in self.employees]
        return {
            "count": len(salaries),
            "total": sum(salaries),
            "average": sum(salaries) / len(salaries),
            "max": max(salaries),
            "min": min(salaries)
        }

    def show_all(self):    #Показать всех сотрудников
        if not self.employees:
            print("Список сотрудников пуст")
            return
        print("\nСписок сотрудников:")
        for i, emp in enumerate(self.employees, 1):
            print(f"{i}. {emp}")