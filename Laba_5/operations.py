from functools import reduce


def filter_objects(objects, predicate): #Функция высшего порядка: фильтрация по предикату
    return list(filter(predicate, objects))

def transform_objects(objects, operation): #Функция высшего порядка: преобразование объектов
    return list(map(operation, objects))

def sort_objects(objects, key_function, reverse=False):    #Сортировка с функцией-ключом
    return sorted(objects, key=key_function, reverse=reverse)

def get_positions(objects):    #Список уникальных должностей (comprehension + set)
    return sorted({obj.position for obj in objects})


def find_highest_paid(objects):    #Поиск самого высокооплачиваемого через reduce
    if not objects:
        return None
    return reduce(
        lambda a, b: a if a.salary > b.salary else b,
        objects
    )


def has_department(objects, department):   #Проверка наличия сотрудников отдела (any)
    return any(
        obj.department.lower() == department.lower()
        for obj in objects
    )


def all_salaries_positive(objects):   #Проверка, что все зарплаты положительные (all)
    return all(obj.salary > 0 for obj in objects)


def total_salary(objects):  #Общая сумма зарплат через reduce
    if not objects:
        return 0
    return reduce(lambda a, b: a + b.salary, objects, 0)


def average_salary(objects): #Средняя зарплата
    if not objects:
        return 0
    return total_salary(objects) / len(objects)


def salary_dict(objects):    #Dict comprehension: имя → зарплата
    return {obj.name: obj.salary for obj in objects}