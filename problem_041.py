from problem_027 import is_prime
from problem_032 import is_pandigital


def largest_pandigital_prime():
    # Any 9 or 8 digit pandigital is divisible by 3 (by summing the digits), so
    # we need only check 7-digit pandigitals and below
    for n in range(7654321, 0, -1):
        if is_pandigital(str(n)) and is_prime(n):
            return n


def main():
    return largest_pandigital_prime()
    # 7652413
