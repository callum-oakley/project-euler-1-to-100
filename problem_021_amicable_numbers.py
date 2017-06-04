def divisors(n):
    k = 2
    while k ** 2 <= n:
        if n % k == 0:
            return {a for b in divisors(n // k) for a in (b, k * b)}
        k += 1
    return {1, n}

def d(n):
    return sum(divisors(n) - {n})

def isAmicable(n):
    return d(n) != n and d(d(n)) == n

# sum(n for n in range(1, 10000) if isAmicable(n)) == 31626
