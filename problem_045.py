from itertools import count


def main():
    tris = (n * (n + 1) // 2 for n in count())
    pents = (n * (3 * n - 1) // 2 for n in count())
    hexs = (n * (2 * n - 1) for n in count())
    pent, hex = next(pents), next(hexs)
    for tri in tris:
        while pent < tri:
            pent = next(pents)
        while hex < tri:
            hex = next(hexs)
        if tri > 40755 and tri == pent == hex:
            break
    return tri
    # 1533776805
