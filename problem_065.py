from fractions import Fraction
from itertools import count


def expansion():
    yield from (2, 1)
    for k in count(1):
        yield from (2 * k, 1, 1)


def convergence(a, n):
    if n == 1:
        return Fraction(next(a))
    return next(a) + 1 / convergence(a, n - 1)


def main():
    return sum(int(d) for d in str(convergence(expansion(), 100).numerator))
    # 272
