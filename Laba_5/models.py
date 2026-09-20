class Employee: #Базовый класс сотрудника

    def __init__(self, name, department, position, salary):
        self.name = name
        self.department = department
        self.position = position
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        self._salary = value

    def __str__(self):
        return (f"{self.name} | {self.department} | "
                f"{self.position} | {self.salary:.2f} руб.")


class Developer(Employee):    #Класс разработчика

    def __init__(self, name, department, salary, language, projects_count):
        super().__init__(name, department, "Разработчик", salary)
        self.language = language
        self.projects_count = projects_count

    def __str__(self):
        return (f"{self.name} | {self.department} | Разработчик | "
                f"{self.language} | проектов: {self.projects_count} | "
                f"{self.salary:.2f} руб.")


class Manager(Employee):    #Класс менеджера

    def __init__(self, name, department, salary, subordinates_count):
        super().__init__(name, department, "Менеджер", salary)
        self.subordinates_count = subordinates_count

    def __str__(self):
        return (f"{self.name} | {self.department} | Менеджер | "
                f"подчинённых: {self.subordinates_count} | "
                f"{self.salary:.2f} руб.")