def primes(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))

def rotations(s):
    return (s[i:] + s[:i] for i in range(1, len(s)))

def circularPrimes(n):
    ps = set(primes(n))
    return (
        p for p in ps
        if all(int(r) in ps for r in rotations(str(p)))
    )

print(len(list(circularPrimes(10 ** 6))))
