def valueOrZero(triangle, i, j):
    if i >= 0 and i < len(triangle) and j >= 0 and j < len(triangle[i]):
        return triangle[i][j]
    return 0

def maximumRoute(triangle):
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(
                valueOrZero(triangle, i - 1, j - 1),
                valueOrZero(triangle, i - 1, j),
            )
    return max(triangle[-1])

def parse(fileName):
    return [
        [int(w) for w in line.split()]
        for line in open(fileName).read().splitlines()
    ]

print(maximumRoute(parse("data/067"))) # 7273
