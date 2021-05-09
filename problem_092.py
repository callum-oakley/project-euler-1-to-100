from functools import cache


@cache
def square_digit_sum(n):
    if n < 10:
        return n ** 2
    return square_digit_sum(int(str(n)[::2])) + square_digit_sum(int(str(n)[1::2]))


@cache
def destination(n):
    if n == 1 or n == 89:
        return n
    return destination(square_digit_sum(n))


def main():
    return sum(1 for n in range(1, 10 ** 7) if destination(n) == 89)
    # 8581146
