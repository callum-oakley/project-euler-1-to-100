from problem_012 import divisors


def d(n):
    return sum(divisors(n) - {n})


def is_amicable(n):
    return n >= 2 and d(n) != n and d(d(n)) == n


def main():
    return sum(n for n in range(10000) if is_amicable(n))
    # 31626
