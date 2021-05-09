from problem_007 import primes

# We know by analysis that to minimise n / phi(n) we want n to be composed of
# as few, large prime factors, as possible, but we also know that n cannot
# itself be prime (because phi(n) would never come out to be a permutation). So
# our best candidates to begin looking at are n of the form p * q, for large
# primes p and q. It turns out the solution is of this form, so we never need
# to look further than this. Having found our potential pair of primes, we can
# show that no triple (etc) produces a smaller n / phi(n), and we are done.

LIMIT = 10 ** 7


def phi(p, q):
    if p == q:
        return p * (p - 1)
    return (p - 1) * (q - 1)


def prime_pairs(ps):
    for p in ps:
        for q in ps:
            if q > p or p * q >= LIMIT:
                break
            yield p, q


def is_permutation(x, y):
    return sorted(str(x)) == sorted(str(y))


def main():
    x = min(
        (
            (p, q)
            for p, q in prime_pairs(list(primes(LIMIT // 2)))
            if is_permutation(phi(p, q), p * q)
        ),
        key=lambda x: x[0] * x[1] / phi(x[0], x[1]),
    )
    return x[0] * x[1]
    # 8319823
