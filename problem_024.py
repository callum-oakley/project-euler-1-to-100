from math import factorial

# We could just use itertools.permutations for this, but this was fun to write.
def permute(xs, n):
    if len(xs) == 0:
        return xs
    granularity = factorial(len(xs) - 1)
    i = n // granularity
    return xs[i] + permute(xs[:i] + xs[i + 1 :], n - i * granularity)


def main():
    return permute("0123456789", 10 ** 6 - 1)
    # 2783915460
