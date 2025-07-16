from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not args and not kwargs:
            all_args = "без аргументов"
        else:
            args_str = [repr(i) for i in args]
            kwargs_str = sorted([f"{k}={v!r}" for k, v in kwargs.items()])
            all_args = ", ".join(args_str + kwargs_str)

        print(f"Вызов: {func.__name__}({all_args})")
        res = func(*args, **kwargs)
        print(f"Результат: {res}")
        return res

    return wrapper
