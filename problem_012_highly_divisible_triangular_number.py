def triangulars():
    n = 0
    while True:
        yield n * (n + 1) // 2
        n += 1

def divisors(n):
    k = 1
    while k ** 2 < n:
        if n % k == 0:
            yield from (k, n // k)
        k += 1

def highlyDivisible(n):
    return next(t for t in triangulars() if len(list(divisors(t))) > n)

# highlyDivisible(500) == 76576500
