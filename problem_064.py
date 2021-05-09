from math import sqrt, gcd


def is_square(n):
    return round(sqrt(n)) ** 2 == n


def period(n):
    # x, y, z represent a number in the form (x*sqrt(n) + y) / z
    x, y, z, seen, i = 1, 0, 1, {}, 0
    while True:
        a = int((x * sqrt(n) + y) / z)
        # Arrived at on paper...
        x, y, z = x * z, z * (a * z - y), x ** 2 * n - (a * z - y) ** 2
        d = gcd(gcd(x, y), z)
        x, y, z = x // d, y // d, z // d
        if (x, y, z) in seen:
            return i - seen[(x, y, z)]
        seen[(x, y, z)] = i
        i += 1


def main():
    return sum(
        1
        for p in (period(n) for n in (m for m in range(10001) if not is_square(m)))
        if p % 2
    )
    # 1322
