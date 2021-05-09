from itertools import count


def search(multiples):
    for x in count(1):
        if len({tuple(sorted(str(k * x))) for k in multiples}) == 1:
            return x


def main():
    return search([1, 2, 3, 4, 5, 6])
    # 142857
