def fibonacci(bound):
    a, b = 0, 1
    while b <= bound:
        yield b
        a, b = b, a + b


def sum_of_even(n):
    return sum(f for f in fibonacci(n) if f % 2 == 0)

print(sum_of_even(4 * 10 ** 6))
