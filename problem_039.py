from math import gcd

def triple(m, n, k):
    return (k * (m ** 2 - n ** 2), k * 2 * m * n, k * (m ** 2 + n ** 2))

def coprime(n, m):
    return gcd(n, m) == 1

def bothOdd(n, m):
    return n % 2 > 0 and m % 2 > 0

def triples(maxP):
    # Follows Euclid's formula
    m, n, k = 2, 1, 1
    while sum(triple(m, n, k)) <= maxP:
        while n < m:
            if coprime(n, m) and not bothOdd(n, m):
                while sum(triple(m, n, k)) <= maxP:
                    yield triple(m, n, k)
                    k += 1
            n, k = n + 1, 1
        m, n = m + 1, 1

solutionCounts = {p: 0 for p in range(1, 1001)}
for t in triples(1000):
    solutionCounts[sum(t)] += 1

print(max(solutionCounts, key=solutionCounts.get))
