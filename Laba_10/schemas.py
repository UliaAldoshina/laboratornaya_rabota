from exceptions import ValidationError


def validate_book_data(data: dict, is_patch: bool = False):
    if not isinstance(data, dict):
        raise ValidationError("Тело запроса должно быть JSON-объектом")

    if not is_patch:
        required_fields = ["title", "author", "year", "genre", "price"]
        for field in required_fields:
            if field not in data:
                raise ValidationError(f"Отсутствует обязательное поле: '{field}'")

    if "title" in data and (not isinstance(data["title"], str) or not data["title"].strip()):
        raise ValidationError("Название книги ('title') не может быть пустым")

    if "author" in data and (not isinstance(data["author"], str) or not data["author"].strip()):
        raise ValidationError("Автор ('author') не может быть пустым")

    if "year" in data:
        try:
            year = int(data["year"])
            if year < 0 or year > 2026:
                raise ValidationError("Указан некорректный год издания")
        except (ValueError, TypeError):
            raise ValidationError("Поле 'year' должно быть целым числом")

    if "price" in data:
        try:
            price = float(data["price"])
            if price < 0:
                raise ValidationError("Цена не может быть отрицательной")
        except (ValueError, TypeError):
            raise ValidationError("Поле 'price' должно быть числом")