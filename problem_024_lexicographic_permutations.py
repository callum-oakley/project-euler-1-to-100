from math import factorial

def permute(xs, n):
    if len(xs) == 1:
        return xs
    granularity = factorial(len(xs) - 1)
    index = n // granularity
    skipped = index * granularity
    return xs[index:index + 1] + permute(
        xs[:index] + xs[index + 1:], n - skipped
    )

print(permute("0123456789", 10 ** 6 - 1)) # 2783915460
