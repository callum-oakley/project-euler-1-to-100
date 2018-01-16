from fractions import Fraction
from math import sqrt, gcd

def inf_range(n=0, step=1):
    while True:
        yield n
        n += step

def expansion(n):
    # x, y, z represent a number in the form (x*sqrt(n) + y) / z
    x, y, z = 1, 0, 1
    while True:
        a = int((x * sqrt(n) + y) / z)
        yield a
        # Arrived at on paper...
        x, y, z = x * z, z * (a * z - y), x ** 2 * n - (a * z - y) ** 2
        d = gcd(gcd(x, y), z)
        x, y, z = x // d, y // d, z // d

def convergence(a, i):
    if i == 1:
        return Fraction(next(a))
    return next(a) + 1 / convergence(a, i - 1)

# https://en.wikipedia.org/wiki/Pell's_equation#Fundamental_solution_via_continued_fractions
def solve(d):
    for i in inf_range(1):
        c = convergence(expansion(d), i)
        if c.numerator ** 2 - d * c.denominator ** 2 == 1:
            return c.numerator

def is_square(n):
    return round(sqrt(n)) ** 2 == n

print(max((d for d in range(1001) if not is_square(d)), key=solve))
