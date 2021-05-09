from math import sqrt, ceil
from functools import cache
from itertools import count


# from http://mathworld.wolfram.com/PartitionFunctionP.html with a restriction
# over the range to exclude a lot of the zero terms
@cache
def p(n):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    return sum(
        (1 if k % 2 else -1)
        * (p(n - k * (3 * k - 1) // 2) + p(n - k * (3 * k + 1) // 2))
        for k in range(1, ceil((sqrt(1 + 24 * n) - 1) / 6) + 1)
    )


def main():
    return next(n for n in count() if p(n) % 10 ** 6 == 0)
    # 55374
