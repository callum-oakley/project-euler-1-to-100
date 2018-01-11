from math import ceil, log

def primes(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))

def prime(n):
    # https://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number
    if n < 5:
        bound = 12
    else:
        bound = ceil((n + 1) * (log(n + 1) + log(log(n + 1))))
    return list(primes(bound))[n]

print(prime(10000))
