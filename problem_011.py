def product(xs):
    result = 1
    for x in xs:
        result *= x
    return result


def adjacent_products(grid):
    indices = {(x, y) for x in range(len(grid)) for y in range(len(grid[0]))}
    return (product(grid[x + k * dx][y + k * dy] for k in range(4))
            for x, y in indices
            for dx, dy in ((1, 0), (0, 1), (1, 1), (1, -1))
            if (x + 3 * dx, y + 3 * dy) in indices)


def parse(file):
    return [[int(w) for w in line.split()]
            for line in open(file).read().splitlines()]


print(max(adjacent_products(parse("data/011"))))
