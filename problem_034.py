from math import factorial


def digit_factorials():
    length = 2
    while length * factorial(9) >= 10 ** (length - 1):
        yield from (
            n
            for n in range(10 ** (length - 1), 10 ** length)
            if sum(factorial(int(d)) for d in str(n)) == n
        )
        length += 1


print(sum(digit_factorials()))
