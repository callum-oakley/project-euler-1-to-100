def search(figs, result=None):
    if len(figs) == 0 and result[0] // 100 == result[-1] % 100:
        yield result
    elif result == None:
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

print(sum(next(search({precompute_fig(f) for f in [
    lambda n: n * (n + 1) // 2, # triangle
    lambda n: n ** 2, # square
    lambda n: n * (3 * n - 1) // 2, # pentagonal
    lambda n: n * (2 * n - 1), # hexagonal
    lambda n: n * (5 * n - 3) // 2, # heptagonal
    lambda n: n * (3 * n - 2), # octagonal
]}))))
