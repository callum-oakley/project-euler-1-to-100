from functools import cache

from problem_034 import factorial_digit_sum


@cache
def chain_len(n):
    if n in (871, 45361, 872, 45362):
        return 2
    if n in (169, 363601, 1454):
        return 3
    m = factorial_digit_sum(str(n))
    if m == n:
        return 1
    return 1 + chain_len(m)


def main():
    return sum(1 for n in range(10 ** 6) if chain_len(n) == 60)
    # 402
