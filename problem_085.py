# From some pen on paper combinatorics...
def sub_rectangle_count(n, m):
    return sum((n - np) * (m - mp) for np in range(n) for mp in range(m))


# Starting with m = 1 and n high enough to put sub_rectangle_count(n, m) > 2 million, subtract from
# n until we're below 2 million, then add to m until we're above. Repeating in this way we zig-zag
# along as close as possible to the 2 million mark without making our search unnecessarily large.
def search_space():
    n, m = 2000, 1
    count = sub_rectangle_count(n, m)

    while True:
        while count > 2 * 10 ** 6:
            n -= 1
            if n < 1:
                return
            count = sub_rectangle_count(n, m)
            yield (n, m, count)

        while count < 2 * 10 ** 6:
            m += 1
            count = sub_rectangle_count(n, m)
            yield (n, m, count)


best_n, best_m, best_count = min(search_space(), key=lambda triplet: abs(triplet[2] - 2 * 10 ** 6))
print(best_n * best_m)
