def inf_range(n=0, step=1):
    while True:
        yield n
        n += step


def search(n):
    seen = {}
    for c in (m ** 3 for m in inf_range()):
        digits = tuple(sorted(str(c)))
        if digits not in seen:
            seen[digits] = set()
        seen[digits] |= {c}
        if len(seen[digits]) >= n:
            return min(seen[digits])


print(search(5))
# 127035954683
