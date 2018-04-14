from math import factorial
from functools import lru_cache


def factorial_digit_sum(n):
    return sum(factorial(int(d)) for d in str(n))


@lru_cache(maxsize=None)
def chain_len(n):
    if n in (871, 45361, 872, 45362):
        return 2
    if n in (169, 363601, 1454):
        return 3
    m = factorial_digit_sum(n)
    if m == n:
        return 1
    return 1 + chain_len(m)


print(sum(1 for n in range(10 ** 6) if chain_len(n) == 60))
