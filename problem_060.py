from functools import cache
from math import sqrt, log10

from problem_007 import primes

LIMIT = 10 ** 7


def is_prime(n):
    if n < LIMIT:
        return n in ps
    for p in pl:
        if p > sqrt(n):
            return True
        if n % p == 0:
            return False
    raise ValueError("ran out of small primes!")


def concat(p, q):
    return p * 10 ** (int(log10(q)) + 1) + q


@cache
def is_compatable(p, q):
    return is_prime(concat(p, q)) and is_prime(concat(q, p))


def main():
    global pl, ps
    pl = list(primes(LIMIT))
    ps = set(pl)

    candidates = (
        (pl[a], pl[b], pl[c], pl[d], pl[e])
        for a in range(len(pl))
        for b in range(a)
        if is_compatable(pl[a], pl[b])
        for c in range(b)
        if all(is_compatable(pl[x], pl[c]) for x in [a, b])
        for d in range(c)
        if all(is_compatable(pl[x], pl[d]) for x in [a, b, c])
        for e in range(d)
        if all(is_compatable(pl[x], pl[e]) for x in [a, b, c, d])
    )

    return sum(next(candidates))
    # 26033
