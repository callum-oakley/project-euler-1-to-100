def divisors(n):
    k = 2
    while k ** 2 <= n:
        if n % k == 0:
            return {a for b in divisors(n // k) for a in (b, k * b)}
        k += 1
    return {1, n}

def isAbundant(n):
    return sum(divisors(n) - {n}) > n

def abundantSums(bound):
    abundants = list(n for n in range(1, bound) if isAbundant(n))
    return {a + b for a in abundants for b in abundants}

print(sum(set(range(1, 28124)) - abundantSums(28124)))
