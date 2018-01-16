from fractions import Fraction

def inf_range(n=0, step=1):
    while True:
        yield n
        n += step

def expansion():
    yield from (2, 1)
    for k in inf_range(1):
        yield from (2 * k, 1, 1)

def convergence(a, n):
    if n == 1:
        return Fraction(next(a))
    return next(a) + 1 / convergence(a, n - 1)

print(sum(int(d) for d in str(convergence(expansion(), 100).numerator)))
