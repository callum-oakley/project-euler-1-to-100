def is_pandigital(s):
    return {int(d) for d in s} == set(range(1, len(s) + 1))


def pandigital_products():
    a = 1
    while len(str(a) + str(a + 1) + str(a * (a + 1))) < 10:
        b = a + 1
        while len(s := str(a) + str(b) + str(a * b)) < 10:
            if len(s) == 9 and is_pandigital(s):
                yield a * b
            b += 1
        a += 1


def main():
    return sum(set(pandigital_products()))
    # 45228
