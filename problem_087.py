from math import sqrt

from problem_007 import primes


def f(p2, p3, p4):
    return p2 ** 2 + p3 ** 3 + p4 ** 4


def main():
    LIMIT = 5 * 10 ** 7

    ps = list(primes(round(sqrt(LIMIT))))
    expressible = set()

    for p2 in ps:
        if f(p2, 2, 2) >= LIMIT:
            break
        for p3 in ps:
            if f(p2, p3, 2) >= LIMIT:
                break
            for p4 in ps:
                if f(p2, p3, p4) >= LIMIT:
                    break
                expressible.add(f(p2, p3, p4))

    return len(expressible)
    # 1097343
