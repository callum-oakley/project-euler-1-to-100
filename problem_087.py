from math import sqrt

LIMIT = 5 * 10 ** 7


def prime_gen(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))


primes = list(prime_gen(round(sqrt(LIMIT))))


def f(p2, p3, p4):
    return p2 ** 2 + p3 ** 3 + p4 ** 4


expressible = set()

for p2 in primes:
    if f(p2, 2, 2) >= LIMIT:
        break
    for p3 in primes:
        if f(p2, p3, 2) >= LIMIT:
            break
        for p4 in primes:
            if f(p2, p3, p4) >= LIMIT:
                break
            expressible.add(f(p2, p3, p4))

print(len(expressible))
# 1097343
