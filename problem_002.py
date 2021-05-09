from functools import cache


@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    total = 0
    n = 1
    while (f := fib(n)) <= 4 * 10 ** 6:
        if f % 2 == 0:
            total += f
        n += 1

    return total
    # 4613732
