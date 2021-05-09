from functools import cache


@cache
def collatz(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + collatz(n // 2)
    return 1 + collatz(3 * n + 1)


def main():
    return max((n for n in range(1, 10 ** 6)), key=collatz)
    # 837799
