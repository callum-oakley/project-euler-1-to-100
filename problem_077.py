from math import inf
from functools import cache
from itertools import count, takewhile

from problem_007 import primes


@cache
def decompositions(n, max_part=inf):
    return (1 if n <= max_part and n in ps else 0) + sum(
        decompositions(n - m, m)
        for m in takewhile(lambda p: p < min(max_part + 1, n), ps)
    )


def main():
    global ps
    ps = list(primes(5000))
    return next(n for n in count() if decompositions(n) - 1 > 5000)
    # 71
