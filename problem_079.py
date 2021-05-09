from itertools import permutations


def is_subsequence(x, y):
    it = iter(y)
    return all(c in it for c in x)


def main():
    logins = [line.strip() for line in open("data/079").readlines()]
    digits = "".join({d for login in logins for d in login})
    return next(
        "".join(guess)
        for guess in permutations(digits)
        if all(is_subsequence(login, guess) for login in logins)
    )
    # 73162890
