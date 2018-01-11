from math import ceil, sqrt
from functools import lru_cache

@lru_cache(maxsize=None)
def isPrime(n):
    if n <= 1:
        return False
    for divisor in range(2, ceil(sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True

def growLeft(n):
    return (g for g in (int(str(d) + str(n)) for d in range(10)) if isPrime(g))

def growRight(n):
    return (g for g in (int(str(n) + str(d)) for d in range(10)) if isPrime(g))

def truncatablePrimes():
    leftTruncatable, rightTruncatable = {2, 3, 5, 7}, {2, 3, 5, 7}
    # The existence of a truncatable prime of length n + 1 implies the
    # existence of both a left and right truncatable prime of length n, so as
    # soon as we don't have both left and right truncatable primes of length n,
    # we can stop looking.
    while len(leftTruncatable) > 0 and len(rightTruncatable) > 0:
        leftTruncatable = {n for l in leftTruncatable for n in growLeft(l)}
        rightTruncatable = {n for r in rightTruncatable for n in growRight(r)}
        yield from rightTruncatable & leftTruncatable

print(sum(truncatablePrimes())) # 748317
