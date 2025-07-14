from functools import wraps


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        for i in all_args:
            if i < 0:
                raise ValueError("Все аргументы должны быть положительными")
        return func(*args, *kwargs)
    return wrapper
