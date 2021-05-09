from math import prod

from problem_047 import sieve_prime_factors


def phi(n, ps):
    return round(n * prod(1 - 1 / p for p in ps))


def main():
    pfs = sieve_prime_factors(10 ** 6 + 1)
    return sum(phi(n, pfs[n]) for n in range(2, 10 ** 6 + 1))
    # 303963552391
