from functools import cache
from math import inf


@cache
def p(n):
    return n * (3 * n - 1) // 2


def main():
    # We can stop searching when the difference between each pentagonal number
    # is greater than the smallest difference we have found so far. The
    # solution as actually found very early, and most of the running time is in
    # exhausting all the rest of the possibilities...
    n, pentagonals, max_n, min_difference = 2, set(), 0, inf
    while p(n) - p(n - 1) < min_difference:
        m = n - 1
        while m > 0 and p(n) - p(m) < min_difference:
            while p(max_n) < p(n) + p(m):
                max_n += 1
                pentagonals.add(p(max_n))
            if p(n) - p(m) in pentagonals and p(n) + p(m) in pentagonals:
                min_difference = p(n) - p(m)
            m -= 1
        n += 1
    return min_difference
    # 5482660
