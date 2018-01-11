from math import ceil, sqrt

def isPrime(n):
    if n <= 1:
        return False
    for divisor in range(2, ceil(sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True

def isPandigital(s):
    return {int(d) for d in s} == set(range(1, len(s) + 1))

def largestPandigitalPrime():
    # Any 9 or 8 digit pandigital is divisible by 3 (by summing the digits), so
    # we need only check 7-digit pandigitals and below
    for n in range(7654321, 0, -1):
        if isPandigital(str(n)) and isPrime(n):
            return n

print(largestPandigitalPrime())
