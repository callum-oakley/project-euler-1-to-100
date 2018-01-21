from fractions import Fraction

def candidates(max_d, target):
    for d in range(1, max_d + 1):
        f = Fraction(d * target.numerator // target.denominator, d)
        if 0 < f < target:
            yield f

print(max(candidates(10 ** 6, Fraction(3, 7))))
