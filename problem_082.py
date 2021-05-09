from functools import cache


def in_range(x, y):
    return 0 <= x <= len(matrix) - 1 and 0 <= y <= len(matrix) - 1


@cache
def min_path(x, y, previous_position=None):
    paths_to_here = [
        min_path(xp, yp, previous_position=(x, y))
        for xp, yp in [(x - 1, y), (x, y - 1), (x, y + 1)]
        if (xp, yp) != previous_position and in_range(xp, yp)
    ]

    if x > 0 and len(paths_to_here) > 0:
        return matrix[y][x] + min(paths_to_here)

    return matrix[y][x]


def main():
    global matrix
    matrix = [
        [int(w) for w in line.split(",")]
        for line in open("data/082").readlines()
    ]
    return min(min_path(len(matrix) - 1, y) for y in range(len(matrix)))
    # 260324
