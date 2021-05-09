def primes(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))


def nth(it, n):
    for _ in range(n):
        next(it)
    return next(it)


def main():
    return nth(primes(10 ** 6), 10000)
    # 104743
