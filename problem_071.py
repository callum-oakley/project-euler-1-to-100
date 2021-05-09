from fractions import Fraction


def main():
    target = Fraction(3, 7)
    return max(
        f
        for f in (Fraction(d * 3 // 7, d) for d in range(1, 10 ** 6 + 1))
        if 0 < f < target
    ).numerator
    # 428570
