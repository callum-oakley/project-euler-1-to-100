from math import factorial
from functools import cache


@cache
def factorial_digit_sum(s):
    if len(s) == 1:
        return factorial(int(s))
    return factorial_digit_sum(s[::2]) + factorial_digit_sum(s[1::2])


def main():
    total, length = 0, 2
    while length * factorial(9) >= 10 ** (length - 1):
        for n in range(10 ** (length - 1), 10 ** length):
            if factorial_digit_sum(str(n)) == n:
                total += n
        length += 1
    return total
    # 40730
