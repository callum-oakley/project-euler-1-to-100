def fibonacci(bound):
    a, b = 0, 1
    while b <= bound:
        yield b
        a, b = b, a + b

def sumOfEven(n):
    return sum(f for f in fibonacci(n) if f % 2 == 0)

print(sumOfEven(4 * 10 ** 6))
