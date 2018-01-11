def genPrimes(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))

def longestPrimeSum(bound):
    primes = set(genPrimes(bound))
    primeSeq, longest = sorted(list(primes)), []
    for i in range(len(primeSeq)):
        j = i + len(longest) + 1
        while j < len(primeSeq) and sum(primeSeq[i:j]) < bound:
            if sum(primeSeq[i:j]) in primes:
                longest = primeSeq[i:j]
            j += 1
    return longest

print(sum(longestPrimeSum(10 ** 6)))
