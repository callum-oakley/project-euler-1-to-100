from fractions import Fraction

count = 0
approx = Fraction(1)
for n in range(1000):
    approx = 1 + 1 / (1 + approx)
    if len(str(approx.numerator)) > len(str(approx.denominator)):
        count += 1
print(count)
