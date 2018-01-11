from math import gcd

def smallestMultiple(divisors):
    candidate = 1
    for divisor in divisors:
        candidate *= divisor // gcd(candidate, divisor)
    return candidate

print(smallestMultiple(range(1, 21)))
