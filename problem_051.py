from functools import lru_cache


def gen_primes(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))


@lru_cache(maxsize=None)
def int_to_pattern(n):
    # Each pattern is just n written in base 11
    if n == 0:
        return ""
    if n % 11 == 10:
        return int_to_pattern(n // 11) + "*"
    return int_to_pattern(n // 11) + str(n % 11)


def expand(pattern):
    return (
        int(r)
        for r in (pattern.replace("*", str(d)) for d in range(10))
        if len(r) == len(pattern)
    )


def find_smallest_member(matches):
    bound = 2
    while True:
        primes = set(gen_primes(10 ** bound))
        for pattern in (int_to_pattern(n) for n in range(1, 11 ** bound)):
            prime_replacements = {n for n in expand(pattern) if n in primes}
            if len(prime_replacements) == matches:
                return min(prime_replacements)
        bound += 1


print(find_smallest_member(8))
