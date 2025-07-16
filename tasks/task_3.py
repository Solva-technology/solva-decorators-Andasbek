from functools import wraps


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        for key in all_args:
            if key <= 0:
                raise ValueError("Все аргументы должны быть положительными")
            if not isinstance(key, (int, float)):
                raise TypeError("Все аргументы должны быть числовыми")
        return func(*args, **kwargs)
    return wrapper
