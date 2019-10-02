from functools import lru_cache
from math import sqrt, log10
from bisect import bisect_left

LIMIT = 10 ** 7


def prime_gen(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))


primes = [p for p in prime_gen(LIMIT)]


def in_sorted(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    return False


def is_prime(n):
    if n < LIMIT:
        return in_sorted(primes, n)
    for p in primes:
        if p > sqrt(n):
            return True
        if n % p == 0:
            return False
    raise ValueError("ran out of small primes!")


def concat(p, q):
    return p * 10 ** (int(log10(q)) + 1) + q


@lru_cache(maxsize=None)
def is_compatable(p, q):
    return is_prime(concat(p, q)) and is_prime(concat(q, p))


candidates = (
    (primes[a], primes[b], primes[c], primes[d], primes[e])
    for a in range(len(primes))
    for b in range(a)
    if is_compatable(primes[a], primes[b])
    for c in range(b)
    if all(is_compatable(primes[x], primes[c]) for x in [a, b])
    for d in range(c)
    if all(is_compatable(primes[x], primes[d]) for x in [a, b, c])
    for e in range(d)
    if all(is_compatable(primes[x], primes[e]) for x in [a, b, c, d])
)

print(sum(next(candidates)))
