def reciprocal_cycle(denominator):
    long_division = [(0, 1)]
    while True:
        digit, remainder = divmod(long_division[-1][1] * 10, denominator)
        for i in range(len(long_division)):
            if long_division[-1 - i] == (digit, remainder):
                return [digit for digit, _ in long_division[-1 - i :]]
        long_division.append((digit, remainder))


def reciprocal_cycle_len(denominator):
    return len(reciprocal_cycle(denominator))


print(max(range(1, 1000), key=reciprocal_cycle_len))
# 983
