def divisors(n):
    k = 2
    while k ** 2 <= n:
        if n % k == 0:
            return {a for b in divisors(n // k) for a in (b, k * b)}
        k += 1
    return {1, n}


def is_abundant(n):
    return sum(divisors(n) - {n}) > n


def abundant_sums(bound):
    abundants = list(n for n in range(1, bound) if is_abundant(n))
    return {a + b for a in abundants for b in abundants}


print(sum(set(range(1, 28124)) - abundant_sums(28124)))
# 4179871
