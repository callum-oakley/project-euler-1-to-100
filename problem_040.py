from math import prod


def champernowne():
    n = 0
    while True:
        yield from (int(d) for d in str(n))
        n += 1


def nths(it, ns):
    for i, x in enumerate(it):
        if i > max(ns):
            break
        if i in ns:
            yield x


def main():
    return prod(nths(champernowne(), {10 ** i for i in range(7)}))
    # 210
