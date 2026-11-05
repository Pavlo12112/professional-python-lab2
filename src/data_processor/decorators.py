"""Decorators used by the application."""

from collections import deque
from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import Any


def measure_time(func: Callable) -> Callable:
    """Print the execution time of the decorated function."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f"[time] {func.__name__}: {elapsed:.8f} s")
        return result

    return wrapper


def repeat(count: int) -> Callable:
    """Parametrized decorator: call the function ``count`` times."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = None
            for _ in range(count):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


def record_history(history: deque) -> Callable:
    """Parametrized decorator: remember names of called operations.

    ``history`` is a deque with ``maxlen``, so only the last operations
    are stored.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            history.append(func.__name__)
            return func(*args, **kwargs)

        return wrapper

    return decorator
