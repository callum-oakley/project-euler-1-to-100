from problem_012 import divisors


def is_prime(n):
    return n >= 2 and divisors(n) == {1, n}


def consecutive_primes(a_b):
    a, b = a_b
    n = 0
    while is_prime(n ** 2 + a * n + b):
        n += 1
    return n


def main():
    max_n = None
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            while is_prime(n ** 2 + a * n + b):
                n += 1
            if not max_n or n > max_n:
                max_n, best_a, best_b = n, a, b

    return best_a * best_b
    # -59231
