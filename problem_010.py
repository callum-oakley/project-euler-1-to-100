def primes(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))


print(sum(primes(2 * 10 ** 6)))
# 142913828922
