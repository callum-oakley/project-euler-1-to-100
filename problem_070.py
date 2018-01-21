# We know by analysis that to minimise n / phi(n) we want n to be composed of
# as few, large prime factors, as possible, but we also know that n cannot
# itself be prime (because phi(n) would never come out to be a permutation). So
# our best candidates to begin looking at are n of the form p * q, for large
# primes p and q. It turns out the solution is of this form, so we never need
# to look further than this. Having found our potential pair of primes, we can
# show that no triple (etc) produces a smaller n / phi(n), and we are done.

LIMIT = 10 ** 7

def prime_gen(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))

primes = list(prime_gen(LIMIT // 2))

def phi(p, q):
    if p == q:
        return p * (p - 1)
    return (p - 1) * (q - 1)

def prime_pairs():
    for p in primes:
        for q in primes:
            if q > p or p * q >= LIMIT:
                break
            yield p, q

def permutation(x, y):
    return sorted(str(x)) == sorted(str(y))

x = min(
    ((p, q) for p, q in prime_pairs() if permutation(phi(p, q), p * q)),
    key=lambda x: x[0] * x[1] / phi(x[0], x[1]),
)
print(x[0] * x[1])
