from math import factorial

def choose(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

print(sum(1 for n in range(101) for r in range(n + 1) if choose(n, r) > 1e6))
