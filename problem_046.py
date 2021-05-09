from math import floor, sqrt

from problem_007 import primes


def minimum_counter_example():
    bound, composites, sums = 2, set(), set()
    while not composites - sums:
        ps = set(primes(bound))
        composites = {n for n in range(2, bound) if n % 2 != 0} - ps
        sums = {p + 2 * n ** 2 for p in ps for n in range(floor(sqrt(bound / 2)) + 1)}
        bound *= 2
    return min(composites - sums)


def main():
    return minimum_counter_example()
    # 5777
