def prime_gen(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))

def very_prime_divisible(n):
    v, prime = 1, prime_gen(n)
    while True:
        p = next(prime)
        if p * v > n:
            return v
        else:
            v *= p

# Maximizing n / phi(n) is equivalent to maximizing the product of p / (p - 1)
# for all primes dividing n, by Euler's product formula
# [https://en.m.wikipedia.org/wiki/Euler's_totient_function#Euler's_product_formula].
# p / (p - 1) is largest for small primes, so is maximized for n of the form
#     2 * 3 * 5 * 7 * ...

print(very_prime_divisible(10 ** 6))
