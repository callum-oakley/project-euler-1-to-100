from functools import lru_cache


def parse(file):
    return [[int(w) for w in line.split(',')]
            for line in open(file).read().splitlines()]


@lru_cache(maxsize=None)
def min_path(x, y, direction=None):
    if x == 0:
        return matrix[y][x]
    elif y == 0:
        # It's never beneficial to backtrack, so don't allow it (this also avoids
        # getting stuck in a recursive loop).
        if direction == 'down':
            return matrix[y][x] + min_path(x - 1, y)
        else:
            return matrix[y][x] + min(
                min_path(x - 1, y), min_path(x, y + 1, direction='up'))
    elif y == n - 1:
        if direction == 'up':
            return matrix[y][x] + min_path(x - 1, y)
        else:
            return matrix[y][x] + min(
                min_path(x - 1, y), min_path(x, y - 1, direction='down'))
    else:
        if direction == 'up':
            return matrix[y][x] + min(
                min_path(x - 1, y), min_path(x, y + 1, direction='up'))
        elif direction == 'down':
            return matrix[y][x] + min(
                min_path(x - 1, y), min_path(x, y - 1, direction='down'))
        else:
            return matrix[y][x] + min(
                min_path(x - 1, y), min_path(x, y - 1, direction='down'),
                min_path(x, y + 1, direction='up'))


matrix = parse('data/082')
n = len(matrix)
print(min(min_path(n - 1, y) for y in range(n)))
