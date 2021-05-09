from itertools import count


def search(n):
    seen = {}
    for c in (m ** 3 for m in count()):
        digits = tuple(sorted(str(c)))
        if digits not in seen:
            seen[digits] = set()
        seen[digits] |= {c}
        if len(seen[digits]) >= n:
            return min(seen[digits])


def main():
    return search(5)
    # 127035954683
