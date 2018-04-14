def prime_factors(n):
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            yield divisor
            n //= divisor
        divisor += 1


print(max(prime_factors(600851475143)))
