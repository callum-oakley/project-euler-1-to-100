from functools import lru_cache


def parse(file):
    return [[int(w) for w in line.split(',')]
            for line in open(file).read().splitlines()]


@lru_cache(maxsize=None)
def min_path(x, y):
    if x > 0 and y > 0:
        return matrix[y][x] + min(min_path(x - 1, y), min_path(x, y - 1))
    elif x > 0:
        return matrix[y][x] + min_path(x - 1, y)
    elif y > 0:
        return matrix[y][x] + min_path(x, y - 1)
    else:
        return matrix[y][x]


matrix = parse('data/081')
n = len(matrix)
print(min_path(n - 1, n - 1))
