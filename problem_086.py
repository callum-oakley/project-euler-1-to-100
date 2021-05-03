# Consider cuboids with sides x, y, z, and shortest path p. Given x >= y >= z:
#
#     p ** 2 = x ** 2 + (y + z) ** 2                                         [0]
#
# Let y + z = w, then if we find a solution to
#
#     p ** 2 = x ** 2 + w ** 2                                               [1]
#
# We have found floor(w / 2) - max(w - x - 1, 0) solutions to [0].
#
#     z = 1 + max(w - x - 1, 0), y = w - z                                   [2]
#     z = 2 + max(w - x - 1, 0), y = w - z
#     ...
#     z = floor(w / 2),          y = w - z                                   [3]
#
# To convince yourself of [2]: observe that y <= x so w - z <= x i.e.
#
#     z >= w - x
#     z >= 1 + (w - x - 1)
#
# And [3] follows immediately from y >= z.
#
# The final observation is that since p > w, we can keep our search space
# manageable by ranging over p and x, and deriving w.

from math import sqrt, floor

count = 0
x = 1
while True:
    p = x + 1
    w_squared = p ** 2 - x ** 2
    while w_squared <= (2 * x) ** 2:
        w_squared = p ** 2 - x ** 2
        w = round(sqrt(w_squared))
        if w <= 2 * x and w ** 2 == w_squared:
            count += floor(w / 2) - max(w - x - 1, 0)
            if count > 10 ** 6:
                print(x)
                exit()
        p += 1
    x += 1
# 1818
