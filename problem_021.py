def divisors(n):
    k = 2
    while k ** 2 <= n:
        if n % k == 0:
            return {a for b in divisors(n // k) for a in (b, k * b)}
        k += 1
    return {1, n}


def d(n):
    return sum(divisors(n) - {n})


def is_amicable(n):
    return d(n) != n and d(d(n)) == n


print(sum(n for n in range(2, 10000) if is_amicable(n)))
# 31626
