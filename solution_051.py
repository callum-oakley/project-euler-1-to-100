from functools import lru_cache

def genPrimes(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))

@lru_cache(maxsize=None)
def intToPattern(n):
    # Each pattern is just n written in base 11
    if n == 0:
        return ""
    if n % 11 == 10:
        return intToPattern(n // 11) + "*"
    return intToPattern(n // 11) + str(n % 11)

def expand(pattern):
    return (
        int(r) for r in (pattern.replace("*", str(d)) for d in range(10))
        if len(r) == len(pattern)
    )

def findSmallestMember(matches):
    bound = 2
    while True:
        primes = set(genPrimes(10 ** bound))
        for pattern in (intToPattern(n) for n in range(1, 11 ** bound)):
            primeReplacements = {n for n in expand(pattern) if n in primes}
            if len(primeReplacements) == matches:
                return min(primeReplacements)
        bound += 1

print(findSmallestMember(8)) # 121313
