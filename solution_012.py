def triangulars():
    n = 0
    while True:
        yield n * (n + 1) // 2
        n += 1

def divisors(n):
    k = 2
    while k ** 2 <= n:
        if n % k == 0:
            return {a for b in divisors(n // k) for a in (b, k * b)}
        k += 1
    return {1, n}

def highlyDivisible(n):
    return next(t for t in triangulars() if len(list(divisors(t))) > n)

print(highlyDivisible(500)) # 76576500
