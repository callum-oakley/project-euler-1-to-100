def prime_factors(n):
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            yield divisor
            n //= divisor
        divisor += 1


def main():
    return max(prime_factors(600851475143))
    # 6857
