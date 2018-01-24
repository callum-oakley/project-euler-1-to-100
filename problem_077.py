from math import inf
from functools import lru_cache

def prime_gen(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))

primes = list(prime_gen(5000))

def prime_range(lower, upper):
    for p in primes:
        if p < lower:
            continue
        if p >= upper:
            break
        yield p

def inf_range(n=0, step=1):
    while True:
        yield n
        n += step

@lru_cache(maxsize=None)
def decompositions(n, max_part=inf):
    return (1 if n <= max_part and n in primes else 0) + sum(
        decompositions(n - m, m) for m in prime_range(1, min(max_part + 1, n))
    )

print(next(n for n in inf_range() if decompositions(n) - 1 > 5000))
