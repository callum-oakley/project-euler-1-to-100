from math import ceil, sqrt
from functools import lru_cache


@lru_cache(maxsize=None)
def is_prime(n):
    if n <= 1:
        return False
    for divisor in range(2, ceil(sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True


def grow_left(n):
    return (g for g in (int(str(d) + str(n)) for d in range(10)) if is_prime(g))


def grow_right(n):
    return (g for g in (int(str(n) + str(d)) for d in range(10)) if is_prime(g))


def truncatable_primes():
    left_truncatable, right_truncatable = {2, 3, 5, 7}, {2, 3, 5, 7}
    # The existence of a truncatable prime of length n + 1 implies the
    # existence of both a left and right truncatable prime of length n, so as
    # soon as we don't have both left and right truncatable primes of length n,
    # we can stop looking.
    while len(left_truncatable) > 0 and len(right_truncatable) > 0:
        left_truncatable = {n for l in left_truncatable for n in grow_left(l)}
        right_truncatable = {
            n for r in right_truncatable for n in grow_right(r)
        }
        yield from right_truncatable & left_truncatable


print(sum(truncatable_primes()))
# 748317
