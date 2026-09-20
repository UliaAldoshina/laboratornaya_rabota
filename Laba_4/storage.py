import json
import os
from models import Employee

class Storage:    #Класс для работы с файлом данных

    def __init__(self, filename="employees.json"):
        self.filename = filename

    def save(self, employees):    #Сохранить список сотрудников в JSON
        data = [emp.to_dict() for emp in employees]
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print(f"Данные сохранены в {self.filename}")
        except IOError as error:
            print(f"Ошибка записи файла: {error}")

    def load(self):   #Загрузить список сотрудников из JSON
        if not os.path.exists(self.filename):
            print("Файл данных не найден. Будет создан новый.")
            return []
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
            employees = [Employee.from_dict(item) for item in data]
            print(f"Загружено {len(employees)} сотрудников")
            return employees
        except (IOError, json.JSONDecodeError) as error:
            print(f"Ошибка чтения файла: {error}")
            return []
        except KeyError as error:
            print(f"Некорректная структура данных: {error}")
            return []