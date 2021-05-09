from problem_007 import primes


def grow_left(ps, n):
    return (g for g in (int(str(d) + str(n)) for d in range(10)) if g in ps)


def grow_right(ps, n):
    return (g for g in (int(str(n) + str(d)) for d in range(10)) if g in ps)


def truncatable_primes(ps):
    left, right = {2, 3, 5, 7}, {2, 3, 5, 7}
    # The existence of a truncatable prime of length n + 1 implies the
    # existence of both a left and right truncatable prime of length n, so as
    # soon as we don't have both left and right truncatable primes of length n,
    # we can stop looking.
    while len(left) > 0 and len(right) > 0:
        left = {n for l in left for n in grow_left(ps, l)}
        right = {n for r in right for n in grow_right(ps, r)}
        yield from left & right


def main():
    return sum(truncatable_primes(set(primes(10 ** 6))))
    # 748317
