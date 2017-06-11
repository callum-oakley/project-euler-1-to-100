from math import ceil, sqrt
from functools import lru_cache

@lru_cache(maxsize=None)
def isPrime(n):
    if n <= 1:
        return False
    for divisor in range(2, ceil(sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True

def consecutivePrimes(a_b):
    a, b = a_b
    n = 0
    while isPrime(n ** 2 + a * n + b):
        n += 1
    return n

a, b = max(
    ((a, b) for a in range(-999, 1000) for b in range(-1000, 1001)),
    key=consecutivePrimes
)
print(a * b) # -59231
