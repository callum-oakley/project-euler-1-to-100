from problem_007 import primes


def very_prime_divisible(n):
    v, prime = 1, primes(n)
    while True:
        p = next(prime)
        if p * v > n:
            return v
        else:
            v *= p


def main():
    # Maximizing n / phi(n) is equivalent to maximizing the product of p / (p -
    # 1) for all primes dividing n, by Euler's product formula
    # https://en.m.wikipedia.org/wiki/Euler's_totient_function#Euler's_product_formula
    # p / (p - 1) is largest for small primes, so is maximized for n of the
    # form 2 * 3 * 5 * 7 * ...
    return very_prime_divisible(10 ** 6)
    # 510510
