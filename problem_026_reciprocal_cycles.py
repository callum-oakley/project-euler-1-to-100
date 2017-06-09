def reciprocalCycle(denominator):
    longDivision = [(0, 1)]
    while True:
        longDivision.append(divmod(longDivision[-1][1] * 10, denominator))
        print(longDivision)
        input()

print(reciprocalCycle(7))
