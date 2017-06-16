from functools import lru_cache

def infRange(n=0, step=1):
    while True:
        yield n
        n += step

@lru_cache(maxsize=None)
def distinctPrimeFactors(n):
    if n == 1:
        return set()
    divisor = 2
    while n % divisor != 0:
        divisor += 1
    return {divisor} | distinctPrimeFactors(n // divisor)

print(distinctPrimeFactors(644))
