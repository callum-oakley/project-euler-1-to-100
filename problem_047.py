# Based on the Sieve of Eratosthenes
def sieve_prime_factors(bound):
    res = {i: set() for i in range(1, bound)}
    for i in range(2, bound):
        if not res[i]:  # so i is prime
            for j in range(i, bound, i):
                res[j].add(i)
    return res


def consecutive_runs(ns):
    run = []
    for n in ns:
        if len(run) == 0 or n == run[-1] + 1:
            run.append(n)
        else:
            yield run
            run = [n]
    yield run


def main():
    bound = 2
    runs = []
    while not runs:
        runs = [
            run
            for run in consecutive_runs(
                n for n, pfs in sieve_prime_factors(bound).items() if len(pfs) == 4
            )
            if len(run) == 4
        ]
        bound *= 2
    return runs[0][0]
    # 134043
