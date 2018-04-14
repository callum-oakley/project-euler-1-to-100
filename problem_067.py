def value_or_zero(triangle, i, j):
    if i >= 0 and i < len(triangle) and j >= 0 and j < len(triangle[i]):
        return triangle[i][j]
    return 0


def maximum_route(triangle):
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(value_or_zero(triangle, i - 1, j - 1),
                                  value_or_zero(triangle, i - 1, j))
    return max(triangle[-1])


def parse(file):
    return [[int(w) for w in line.split()]
            for line in open(file).read().splitlines()]


print(maximum_route(parse('data/067')))
