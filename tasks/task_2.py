from functools import wraps


def is_hashable(obj):
    return (
        hasattr(obj, "__hash__")
        and callable(getattr(obj, "__hash__"))
        and obj.__hash__ is not None
    )


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            key = (args, tuple(sorted(kwargs.items())))
            if not is_hashable(key):
                print("Пропуск кэширования: аргументы не хэшируемы")
                return func(*args, **kwargs)
        except Exception as e:
            print(f"Ошибка при создании ключа: {e}")
            return func(*args, **kwargs)

        if key in cache:
            print("Из кэша")
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper
