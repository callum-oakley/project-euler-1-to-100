from math import prod


def windows(n, s):
    for i in range(len(s) - n + 1):
        yield s[i : i + n]


def main():
    digits = open("data/008").read().replace("\n", "")
    return max(prod(int(d) for d in w) for w in windows(13, digits))
    # 23514624000
