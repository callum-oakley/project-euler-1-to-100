LIMIT = 10 ** 6 + 1

prime_divisors = {n: set() for n in range(2, LIMIT)}
for n in range(2, LIMIT):
    if len(prime_divisors[n]) == 0: # n is prime
        k = 1
        while k * n < LIMIT:
            prime_divisors[k * n].add(n)
            k += 1

def phi(n):
    for p in prime_divisors[n]:
        n *= 1 - 1 / p
    return round(n)

print(sum(phi(n) for n in range(2, LIMIT)))
