def primes(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))

fourDigitPrimes = {p for p in primes(10000) if p >= 1000}

def arePrimePermutations(a, b, c):
    digits = sorted(str(a))
    return (
        sorted(str(b)) == digits and sorted(str(c)) == digits and
        b in fourDigitPrimes and c in fourDigitPrimes
    )

primePermutationSequences = (
    [p, p + k, p + 2 * k]
    for p in fourDigitPrimes
    for k in range(2, (10000 - p) // 2 + 1)
    if arePrimePermutations(p, p + k, p + 2 * k)
)

print(next(n for n in (
    "".join(str(p) for p in s) for s in primePermutationSequences
) if n != "148748178147"))
