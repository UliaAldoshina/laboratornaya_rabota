# decorators.py
# Декораторы (журналирование, время, повтор)

import time
from functools import wraps


def log_call(func):  # Декоратор №1: журналирование
    @wraps(func)
    def wrapper(*args, **kwargs):  # Обёртка
        print(f"[LOG] Вызван метод {func.__name__}()")
        result = func(*args, **kwargs)
        return result
    return wrapper


def measure_time(func):  # Декоратор №2: измерение времени
    @wraps(func)
    def wrapper(*args, **kwargs):  # Обёртка
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[PERFORMANCE] {func.__name__}: {elapsed:.4f} сек")
        return result
    return wrapper


def repeat(count: int):  # Декоратор №3: с параметром
    def decorator(func):  # Сам декоратор
        @wraps(func)
        def wrapper(*args, **kwargs):  # Обёртка
            result = None
            for _ in range(count):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator