from math import gcd

def smallestMultiple(divisors):
    candidate = 1
    for divisor in divisors:
        candidate *= divisor // gcd(candidate, divisor)
    return candidate

# smallestMultiple(range(1, 21)) == 232792560
