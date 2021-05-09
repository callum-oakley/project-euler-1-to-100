from math import gcd


def main():
    candidate = 1
    for divisor in range(1, 21):
        candidate *= divisor // gcd(candidate, divisor)
    return candidate
    # 232792560
