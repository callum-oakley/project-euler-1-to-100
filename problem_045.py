def inf_range(n=0, step=1):
    while True:
        yield n
        n += step


def tri_pen_hexs():
    pents = (n * (3 * n - 1) // 2 for n in inf_range(1))
    hexs = (n * (2 * n - 1) for n in inf_range(1))
    pent, hex = next(pents), next(hexs)
    for tri in (n * (n + 1) // 2 for n in inf_range(1)):
        while pent < tri:
            pent = next(pents)
        while hex < tri:
            hex = next(hexs)
        if tri == pent and tri == hex:
            yield tri


print(next(n for n in tri_pen_hexs() if n > 40755))
