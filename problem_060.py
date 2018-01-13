from functools import lru_cache
from math import ceil, sqrt, log10

def primeGen(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))

limit = 10**7
primes = [p for p in primeGen(limit)]
primesS = {p for p in primes}

def isPrime(n):
    if n < limit:
        return n in primesS
    for p in primes:
        if p > sqrt(n):
            return True
        if n % p == 0:
            return False
    raise ValueError("ran out of small primes!")

def concat(p, q):
    return p * 10 ** (int(log10(q)) + 1) + q

@lru_cache(maxsize=None)
def isCompatable(p, q):
    return isPrime(concat(p, q)) and isPrime(concat(q, p))

candidates = (
    (primes[a], primes[b], primes[c], primes[d], primes[e])
    for a in range(len(primes))
    for b in range(a)
    if isCompatable(primes[a], primes[b])
    for c in range(b)
    if all(isCompatable(primes[x], primes[c]) for x in [a, b])
    for d in range(c)
    if all(isCompatable(primes[x], primes[d]) for x in [a, b, c])
    for e in range(d)
    if all(isCompatable(primes[x], primes[e]) for x in [a, b, c, d])
)

print(sum(next(candidates)))
