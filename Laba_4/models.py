from exceptions import NegativeSalaryError


class Employee:    #Класс сотрудника

    def __init__(self, name, position, department, salary):
        self.name = name
        self.position = position
        self.department = department
        self._salary = None
        self.salary = salary

    @property
    def salary(self):  #Геттер зарплаты

        return self._salary

    @salary.setter
    def salary(self, value):    #Сеттер с проверкой
        if value < 0:
            raise NegativeSalaryError(
                f"Зарплата не может быть отрицательной: {value}"
            )
        self._salary = value

    def to_dict(self):    #Преобразование объекта в словарь
        return {
            "name": self.name,
            "position": self.position,
            "department": self.department,
            "salary": self.salary
        }

    @classmethod
    def from_dict(cls, data):    #Создание объекта из словаря
        return cls(
            data["name"],
            data["position"],
            data["department"],
            data["salary"]
        )

    def __str__(self):
        return (f"{self.name} | {self.position} | "
                f"{self.department} | {self.salary:.2f} руб.")