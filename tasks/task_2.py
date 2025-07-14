from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in cache:
            print("Из кэша")
            return cache[args]
        result = func(*args, **kwargs)
        cache[args] = result
        return result

    return wrapper
