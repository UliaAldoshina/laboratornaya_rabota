class BookNotFoundError(Exception):
    """Исключение: книга не найдена."""
    pass


class ValidationError(Exception):
    """Исключение: ошибка валидации входных данных."""
    pass