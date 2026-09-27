# exceptions.py
# Пользовательские исключения


class EntityNotFoundError(Exception):  # Издание не найдено
    pass


class InvalidStatusError(Exception):  # Недопустимое изменение статуса
    pass