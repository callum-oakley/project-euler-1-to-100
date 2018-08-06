from functools import lru_cache


def parse(file):
    return [[int(w) for w in line.split(',')]
            for line in open(file).read().splitlines()]


def in_range(x, y):
    return 0 <= x <= n - 1 and 0 <= y <= n - 1


@lru_cache(maxsize=None)
def min_path(x, y, previous_position=None):
    paths_to_here = [
        min_path(xp, yp, previous_position=(x, y))
        for (xp, yp) in [(x - 1, y), (x, y - 1), (x, y + 1)]
        if (xp, yp) != previous_position and in_range(xp, yp)
    ]

    if x > 0 and len(paths_to_here) > 0:
        return matrix[y][x] + min(paths_to_here)

    return matrix[y][x]


matrix = parse('data/082')
n = len(matrix)
print(min(min_path(n - 1, y) for y in range(n)))
