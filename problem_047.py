def consecutiveRuns(ns):
    run = []
    for n in ns:
        if len(run) == 0 or n == run[-1] + 1:
            run.append(n)
        else:
            yield run
            run = [n]
    yield run

# Based on the Sieve of Eratosthenes
def intsByNoOfPrimeFactors(n, bound):
    primeFactors = {i: set() for i in range(2, bound)}
    for i in range(2, bound):
        if not primeFactors[i]: # so i is prime
            for j in range(2 * i, bound, i):
                primeFactors[j].add(i)
        if len(primeFactors[i]) == n:
            yield i

def firstRunOf(n):
    bound = 2
    runs = []
    while not runs:
        runs = [
            run for run in consecutiveRuns(intsByNoOfPrimeFactors(n, bound))
            if len(run) == n
        ]
        bound *= 2
    return runs[0]

print(firstRunOf(4)[0])
