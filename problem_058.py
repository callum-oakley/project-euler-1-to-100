from math import ceil, sqrt

def isPrime(n):
    if n <= 1:
        return False
    for divisor in range(2, ceil(sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True

total = 13
prime = 8
sideLength = 7
while prime / total >= 0.1:
    sideLength += 2
    total += 4
    for k in range(1, 4):
        prime += 1 if isPrime(sideLength ** 2 - k * (sideLength - 1)) else 0
print(sideLength)
