def fibonacci(bound):
    a, b = 0, 1
    while b <= bound:
        yield b
        a, b = b, a + b


print(sum(f for f in fibonacci(4 * 10 ** 6) if f % 2 == 0))
# 4613732
