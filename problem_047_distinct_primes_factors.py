from functools import lru_cache

def infRange(n=0, step=1):
    while True:
        yield n
        n += step

@lru_cache(maxsize=None)
def distinctPrimeFactors(n):
    if n <= 1:
        return set()
    divisor = 2
    while n % divisor != 0:
        divisor += 1
    return {divisor} | distinctPrimeFactors(n // divisor)

def consecutiveRuns(ns):
    run = []
    for n in ns:
        if len(run) == 0 or n == run[-1] + 1:
            run.append(n)
        else:
            yield run
            run = [n]
    yield run

print(next(
    run[0] for run in consecutiveRuns(
        n for n in infRange()
        if len(distinctPrimeFactors(n)) == 4
    ) if len(run) == 4
)) # 134043
