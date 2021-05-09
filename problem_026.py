def reciprocal_cycle(denominator):
    long_division = [(0, 1)]
    while True:
        digit, remainder = divmod(long_division[-1][1] * 10, denominator)
        for i in range(len(long_division)):
            if long_division[-1 - i] == (digit, remainder):
                return [digit for digit, _ in long_division[-1 - i :]]
        long_division.append((digit, remainder))


def main():
    return max(range(1, 1000), key=lambda d: len(reciprocal_cycle(d)))
    # 983
