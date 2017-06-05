from math import factorial

def permute(xs, n):
    if len(xs) == 1:
        return xs
    granularity = factorial(len(xs) - 1)
    i = n // granularity
    return xs[i] + permute(xs[:i] + xs[i + 1:], n - i * granularity)

print(permute("0123456789", 10 ** 6 - 1)) # 2783915460
