def corners(start, jump):
    return (start + i * jump for i in range(1, 5))

def diagonals(sideLength):
    yield 1
    for ring in range((sideLength - 1) // 2):
        yield from corners((2 * ring + 1) ** 2, 2 * (ring + 1))

print(sum(n for n in diagonals(1001)))
