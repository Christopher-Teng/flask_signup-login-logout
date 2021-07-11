from functools import wraps


def set_query_conditions(**conditions):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for k, v in conditions.items():
                if k not in kwargs.keys():
                    kwargs[k] = v
            return func(*args, **kwargs)
        return wrapper
    return decorator
