def square_difference(ns):
    return sum(ns) ** 2 - sum(n ** 2 for n in ns)


def main():
    return square_difference(range(1, 101))
    # 25164150
