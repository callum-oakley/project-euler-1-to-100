from fractions import Fraction

target = Fraction(3, 7)
print(
    max(
        f
        for f in (Fraction(d * 3 // 7, d) for d in range(1, 10 ** 6 + 1))
        if 0 < f < target
    ).numerator
)
