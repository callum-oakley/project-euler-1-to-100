def primes(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))


four_digit_primes = {p for p in primes(10000) if p >= 1000}


def are_prime_permutations(a, b, c):
    digits = sorted(str(a))
    return (sorted(str(b)) == digits and sorted(str(c)) == digits and
            b in four_digit_primes and c in four_digit_primes)


prime_permutation_sequences = (
    [p, p + k, p + 2 * k]
    for p in four_digit_primes
    for k in range(2, (10000 - p) // 2 + 1)
    if are_prime_permutations(p, p + k, p + 2 * k))

print(next(n for n in (
    "".join(str(p) for p in s) for s in prime_permutation_sequences
) if n != "148748178147"))
