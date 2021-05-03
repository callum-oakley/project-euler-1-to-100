from math import ceil, sqrt


def is_prime(n):
    if n <= 1:
        return False
    for divisor in range(2, ceil(sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True


def is_pandigital(s):
    return {int(d) for d in s} == set(range(1, len(s) + 1))


def largest_pandigital_prime():
    # Any 9 or 8 digit pandigital is divisible by 3 (by summing the digits), so
    # we need only check 7-digit pandigitals and below
    for n in range(7654321, 0, -1):
        if is_pandigital(str(n)) and is_prime(n):
            return n


print(largest_pandigital_prime())
# 7652413
