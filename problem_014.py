from functools import lru_cache

@lru_cache(maxsize=None)
def collatzLength(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + collatzLength(n // 2)
    return 1 + collatzLength(3 * n + 1)

print(max((n for n in range(1, 10 ** 6)), key=collatzLength))
