from functools import lru_cache

@lru_cache(maxsize=None)
def p(n):
    return n * (3 * n - 1) // 2

def pentagonalDifferences():
    n, pentagonals, maxN, difference = 2, set(), 0, float("inf")
    # We can stop searching when the difference between each pentagonal number
    # is greater than the smallest difference we have found so far. The
    # solution as actually found very early, and most of the running time is in
    # exhausting all the rest of the possibilities...
    while p(n) - p(n - 1) < difference:
        m = n - 1
        while m > 0 and p(n) - p(m) < difference:
            while p(maxN) < p(n) + p(m):
                maxN += 1
                pentagonals.add(p(maxN))
            if p(n) + p(m) in pentagonals and p(n) - p(m) in pentagonals:
                difference = p(n) - p(m)
                yield difference
            m -= 1
        n += 1

print(min(pentagonalDifferences())) # 5482660
