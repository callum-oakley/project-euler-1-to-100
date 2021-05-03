def is_right_angled(x1, y1, x2, y2):
    sides_squared = sorted(
        [x1 ** 2 + y1 ** 2, x2 ** 2 + y2 ** 2, (x1 - x2) ** 2 + (y1 - y2) ** 2]
    )
    return sides_squared[2] == sides_squared[0] + sides_squared[1]


# Generate unique triangles by only considering x1, y1, x2, y2 such that
# x1 >= x2, and if x1 == x2 then y1 > y2. i.e. the first point is always to the
# right of or above the second.
def integer_right_triangles(max):
    return [
        (x1, y1, x2, y2)
        for x1 in range(max + 1)
        for y1 in range(max + 1)
        for x2 in range(x1 + 1)
        for y2 in range(max + 1)
        if x1 > x2 or y1 > y2
        if x2 > 0 or y2 > 0
        if is_right_angled(x1, y1, x2, y2)
    ]


print(len(integer_right_triangles(50)))
# 14234
