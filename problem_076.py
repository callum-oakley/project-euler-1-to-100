from math import inf
from functools import cache


@cache
def decompositions(n, max_part=inf):
    return (0 if n > max_part else 1) + sum(
        decompositions(n - m, m) for m in range(1, min(max_part + 1, n))
    )


def main():
    return decompositions(100) - 1  # includes the trivial decomposition
    # 190569291
