def search(figs, result=None):
    if len(figs) == 0 and result[0] // 100 == result[-1] % 100:
        yield result
    elif result is None:
        for n in range(1000, 10000):
            for fig in figs:
                if n in fig:
                    yield from search(figs - {fig}, [n])
    else:
        prefix = result[-1] % 100
        for m in range(10, 100):
            n = prefix * 100 + m
            for fig in figs:
                if n in fig:
                    yield from search(figs - {fig}, result + [n])


# precompute all the figurate numbers that we care about for a given formula
def precompute_fig(f):
    n, fig = 1, []
    while f(n) < 1000:
        n += 1
    while f(n) < 10000:
        fig.append(f(n))
        n += 1
    return frozenset(fig)


def triangle(n):
    return n * (n + 1) // 2


def square(n):
    return n ** 2


def pentagonal(n):
    return n * (3 * n - 1) // 2


def hexagonal(n):
    return n * (2 * n - 1)


def heptagonal(n):
    return n * (5 * n - 3) // 2


def octagonal(n):
    return n * (3 * n - 2)


print(sum(next(search({
    precompute_fig(f)
    for f in [
        triangle, square, pentagonal, hexagonal, heptagonal, octagonal]}))))
