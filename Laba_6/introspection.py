# introspection.py
# Интроспекция объектов

import inspect


def inspect_object(obj) -> None:  # Полная интроспекция
    print("\n" + "=" * 50)
    print("=== ИНФОРМАЦИЯ ОБ ОБЪЕКТЕ ===")
    print("=" * 50)

    print(f"Тип: {type(obj).__name__}")  # 1. type()

    from models import Book, Magazine, EPublication
    if isinstance(obj, Book):  # 2. isinstance()
        print("Класс: Книга")
    elif isinstance(obj, Magazine):
        print("Класс: Журнал")
    elif isinstance(obj, EPublication):
        print("Класс: Электронное издание")
    else:
        print("Класс: Неизвестный")

    print(f"Родитель: {type(obj).__mro__[-2].__name__}")  # 3. issubclass()

    print(f"Есть 'title': {hasattr(obj, 'title')}")  # 4. hasattr()
    print(f"Есть 'pages': {hasattr(obj, 'pages')}")

    print(f"Название: {getattr(obj, 'title', '—')}")  # 5. getattr()
    print(f"Статус: {getattr(obj, 'status', '—')}")

    public = [a for a in dir(obj) if not a.startswith("_")]  # 6. dir()
    print(f"\nПоля и методы ({len(public)}):")
    for attr in public:
        print(f"  - {attr}")

    print("\nСигнатуры методов:")  # 7. inspect.signature()
    for name, method in inspect.getmembers(obj, inspect.ismethod):
        if not name.startswith("_"):
            try:
                print(f"  {name}{inspect.signature(method)}")
            except (ValueError, TypeError):
                pass

    print("=" * 50)