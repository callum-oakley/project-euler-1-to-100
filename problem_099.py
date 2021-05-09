from math import log


def value(base, exp):
    # log preserves order, and log(a ** b) = b * log(a)
    return exp * log(base)


def parse(file):
    for line in open(file).readlines():
        yield (int(x) for x in line.split(","))


def main():
    return max(
        enumerate(parse("data/099"), start=1),
        key=lambda args: value(*args[1]),
    )[0]
    # 709
