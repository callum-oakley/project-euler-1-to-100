from problem_007 import primes


def are_prime_permutations(four_digit_primes, a, b, c):
    return (
        sorted(str(a)) == sorted(str(b)) == sorted(str(c))
        and a in four_digit_primes
        and b in four_digit_primes
        and c in four_digit_primes
    )


def main():
    four_digit_primes = {p for p in primes(10000) if p >= 1000}

    prime_permutation_sequences = (
        [p, p + k, p + 2 * k]
        for p in four_digit_primes
        for k in range(2, (10000 - p) // 2 + 1)
        if are_prime_permutations(four_digit_primes, p, p + k, p + 2 * k)
    )

    return next(
        n
        for n in (
            "".join(str(p) for p in s) for s in prime_permutation_sequences
        )
        if n != "148748178147"
    )
    # 296962999629
