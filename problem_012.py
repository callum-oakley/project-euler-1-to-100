from functools import cache
from itertools import count


@cache
def divisors(n):
    k = 2
    while k ** 2 <= n:
        if n % k == 0:
            return {a for b in divisors(n // k) for a in (b, k * b)}
        k += 1
    return {1, n}


def main():
    triangulars = (n * (n + 1) // 2 for n in count())
    return next(t for t in triangulars if sum(1 for _ in divisors(t)) > 500)
    # 76576500
