from math import sqrt


# generating the first few values in the sequence naively leads us to
# https://oeis.org/A011900
# TODO prove why this is the case
def blue(a, b):
    while True:
        a, b = b, 6 * b - a - 2
        yield b


def search():
    for b in blue(1, 3):
        # TODO this is a hack, calculate total exactly
        total_ish = sqrt(2) * b
        if total_ish > 10 ** 12:
            return b


def main():
    return search()
    # 756872327473
