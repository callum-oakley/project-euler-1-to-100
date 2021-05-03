from math import factorial


def permute(xs, n):
    if len(xs) == 0:
        return xs
    granularity = factorial(len(xs) - 1)
    i = n // granularity
    return xs[i] + permute(xs[:i] + xs[i + 1 :], n - i * granularity)


def inf_range(n=0, step=1):
    while True:
        yield n
        n += step


def is_subsequence(x, y):
    it = iter(y)
    return all(c in it for c in x)


def force(logins):
    for n in inf_range():
        if all(is_subsequence(login, str(n)) for login in logins):
            return n


# Optimistic because it assumes that no digit appears more than once. This
# turns out to be the case.
def optimistic_force(logins):
    digits = "".join(sorted({d for login in logins for d in login}))
    for guess in (permute(digits, n) for n in inf_range()):
        if all(is_subsequence(login, guess) for login in logins):
            return guess


def parse(file):
    return open(file).read().splitlines()


print(optimistic_force(parse("data/079")))
# 73162890
