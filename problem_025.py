from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def naturals():
    n = 0
    while True:
        yield n
        n += 1


print(next(i for i in naturals() if len(str(fibonacci(i))) >= 1000))
