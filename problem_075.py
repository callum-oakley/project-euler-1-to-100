from math import gcd


def inf_range(n=0, step=1):
    while True:
        yield n
        n += step


def pythagorean_triples(limit):
    for n in inf_range(1):
        if 2 * (n + 1) ** 2 + 2 * n * (n + 1) >= limit:
            break
        for m in inf_range(n + 1):
            if 2 * m ** 2 + 2 * m * n >= limit:
                break
            if gcd(n, m) != 1 or n % 2 == 1 and m % 2 == 1:
                continue
            for k in inf_range(1):
                a = k * (m ** 2 - n ** 2)
                b = 2 * k * m * n
                c = k * (m ** 2 + n ** 2)
                if a + b + c >= limit:
                    break
                yield a, b, c


counts = {}
for triple in pythagorean_triples(1500000):
    perim = sum(triple)
    counts[perim] = 1 if perim not in counts else counts[perim] + 1

print(sum(1 for count in counts.values() if count == 1))
