from math import prod


def main():
    grid = [[int(w) for w in line.split()] for line in open("data/011").readlines()]
    indices = {(x, y) for x in range(len(grid)) for y in range(len(grid[0]))}
    return max(
        prod(grid[x + k * dx][y + k * dy] for k in range(4))
        for x, y in indices
        for dx, dy in ((1, 0), (0, 1), (1, 1), (1, -1))
        if (x + 3 * dx, y + 3 * dy) in indices
    )
    # 70600674
