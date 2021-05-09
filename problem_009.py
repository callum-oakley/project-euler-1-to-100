from math import gcd, prod


# Euclid's formula
def pythagorean_triples(limit):
    def triple(n, m, k):
        return k * (m ** 2 - n ** 2), 2 * k * m * n, k * (m ** 2 + n ** 2)

    n = 1
    while sum(triple(n, n + 1, 1)) < limit:
        m = n + 1
        while sum(triple(n, m, 1)) < limit:
            if gcd(n, m) == 1 and (n % 2 == 0 or m % 2 == 0):
                k = 1
                while sum(t := triple(n, m, k)) < limit:
                    yield t
                    k += 1
            m += 1
        n += 1


def main():
    return prod(next(t for t in pythagorean_triples(1001) if sum(t) == 1000))
    # 31875000
