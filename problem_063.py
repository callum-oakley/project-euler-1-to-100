from itertools import count


def powerful():
    for n in count():
        # log10(x) < len(x) for all x, so
        # len(m**n) = n => log10(m**n) < n => log10(m) < 1 => m < 10
        # Furthermore, if 9**n is not long enough for some n, then it won't be
        # long enough for any greater n either, so we can stop searching.
        if len(str(9 ** n)) < n:
            break
        for m in range(1, 10):
            if len(str(m ** n)) > n:
                break
            elif len(str(m ** n)) == n:
                yield m ** n


def main():
    return sum(1 for p in powerful())
    # 49
