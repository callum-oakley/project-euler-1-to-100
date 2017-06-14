from math import floor, sqrt

def primeGen(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))

def minimumCounterexample():
    bound, composites, sums = 2, set(), set()
    while composites - sums == set():
        primes = set(primeGen(bound))
        composites = {n for n in range(2, bound) if n % 2 != 0} - primes
        sums = {
            p + 2 * n ** 2
            for p in primes
            for n in range(floor(sqrt(bound / 2)) + 1)
        }
        bound *= 2
    return min(composites - sums)

print(minimumCounterexample()) # 5777
