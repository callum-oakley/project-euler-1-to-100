def primeFactors(n):
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            yield divisor
            n //= divisor
        divisor += 1

def answer(n):
    return max(primeFactors(n))

# answer(600851475143) = 6857
