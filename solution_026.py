def reciprocalCycle(denominator):
    longDivision = [(0, 1)]
    while True:
        digit, remainder = divmod(longDivision[-1][1] * 10, denominator)
        for i in range(len(longDivision)):
            if longDivision[-1 - i] == (digit, remainder):
                return [digit for digit, _ in longDivision[-1 - i:]]
        longDivision.append((digit, remainder))

def reciprocalCycleLength(denominator):
    return len(reciprocalCycle(denominator))

print(max(range(1, 1000), key=reciprocalCycleLength)) # 983
