def gen_primes(n):
    candidates = set(range(2, n))
    for i in range(2, n):
        if i in candidates:
            yield i
            candidates -= set(range(i, n, i))


def longest_prime_sum(bound):
    primes = set(gen_primes(bound))
    primes_seq, longest = sorted(list(primes)), []
    for i in range(len(primes_seq)):
        j = i + len(longest) + 1
        while j < len(primes_seq) and sum(primes_seq[i:j]) < bound:
            if sum(primes_seq[i:j]) in primes:
                longest = primes_seq[i:j]
            j += 1
    return longest


print(sum(longest_prime_sum(10 ** 6)))
