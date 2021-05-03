from math import gcd


def triple(m, n, k):
    return (k * (m ** 2 - n ** 2), k * 2 * m * n, k * (m ** 2 + n ** 2))


def coprime(n, m):
    return gcd(n, m) == 1


def both_odd(n, m):
    return n % 2 > 0 and m % 2 > 0


def triples(max_p):
    # Follows Euclid's formula
    m, n, k = 2, 1, 1
    while sum(triple(m, n, k)) <= max_p:
        while n < m:
            if coprime(n, m) and not both_odd(n, m):
                while sum(triple(m, n, k)) <= max_p:
                    yield triple(m, n, k)
                    k += 1
            n, k = n + 1, 1
        m, n = m + 1, 1


solution_counts = {p: 0 for p in range(1, 1001)}
for t in triples(1000):
    solution_counts[sum(t)] += 1


print(max(solution_counts, key=solution_counts.get))
# 840
