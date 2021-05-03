from math import inf
from functools import lru_cache


@lru_cache(maxsize=None)
def decompositions(n, max_part=inf):
    return (0 if n > max_part else 1) + sum(
        decompositions(n - m, m) for m in range(1, min(max_part + 1, n))
    )


print(decompositions(100) - 1)  # includes the trivial decomposition
# 190569291
