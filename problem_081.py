from functools import cache


@cache
def min_path(x, y):
    if x > 0 and y > 0:
        return matrix[y][x] + min(min_path(x - 1, y), min_path(x, y - 1))
    elif x > 0:
        return matrix[y][x] + min_path(x - 1, y)
    elif y > 0:
        return matrix[y][x] + min_path(x, y - 1)
    else:
        return matrix[y][x]


def main():
    global matrix
    matrix = [
        [int(w) for w in line.split(",")]
        for line in open("data/081").readlines()
    ]
    return min_path(len(matrix) - 1, len(matrix) - 1)
    # 427337
