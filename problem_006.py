def squareDifference(ns):
    return sum(ns) ** 2 - sum(n ** 2 for n in ns)

print(squareDifference(range(1, 101)))
