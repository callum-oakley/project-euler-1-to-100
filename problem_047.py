def consecutive_runs(ns):
    run = []
    for n in ns:
        if len(run) == 0 or n == run[-1] + 1:
            run.append(n)
        else:
            yield run
            run = [n]
    yield run


# Based on the Sieve of Eratosthenes
def ints_by_no_of_prime_factors(n, bound):
    prime_factors = {i: set() for i in range(2, bound)}
    for i in range(2, bound):
        if not prime_factors[i]:  # so i is prime
            for j in range(2 * i, bound, i):
                prime_factors[j].add(i)
        if len(prime_factors[i]) == n:
            yield i


def first_run_of(n):
    bound = 2
    runs = []
    while not runs:
        runs = [run
                for run in consecutive_runs(
                    ints_by_no_of_prime_factors(n, bound))
                if len(run) == n]
        bound *= 2
    return runs[0]


print(first_run_of(4)[0])
