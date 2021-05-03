from math import gcd


def smallest_multiple(divisors):
    candidate = 1
    for divisor in divisors:
        candidate *= divisor // gcd(candidate, divisor)
    return candidate


print(smallest_multiple(range(1, 21)))
# 232792560
