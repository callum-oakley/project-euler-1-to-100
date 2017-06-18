def genPrimes(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))

def subsequences(s):
    return (s[i:j] for i in range(len(s)) for j in range(len(s)))

def primeSums(bound):
    primes = set(genPrimes(bound))
    return (s for s in subsequences(sorted(list(primes))) if sum(s) in primes)

print(sum(max(primeSums(10000), key=len)))

# Too slow! An easy optimisation to try: if we've found a prime sum containing
# n terms, then we only need to consider subsequent prime sums containing n+1
# terms.
