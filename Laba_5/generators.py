def employees_by_department(objects, department):    #Генератор сотрудников выбранного отдела
    for obj in objects:
        if obj.department.lower() == department.lower():
            yield obj


def high_salary_employees(objects, min_salary):  #Генератор сотрудников с зарплатой выше заданной
    for obj in objects:
        if obj.salary >= min_salary:
            yield obj


def salary_generator(objects):   #Генератор только зарплат
    for obj in objects:
        yield obj.salary


class EmployeeIterator:  #Собственный итератор по сотрудникам

    def __init__(self, objects):
        self.objects = objects
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.objects):
            raise StopIteration
        emp = self.objects[self.index]
        self.index += 1
        return emp