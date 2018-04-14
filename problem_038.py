def is_pandigital(s):
    return len({d for d in s} - {'0'}) == 9


def concat_product(n, m):
    product = ''
    for m in range(1, m + 1):
        product += str(n * m)
    return product


def pandigital_concat_products():
    n = 1
    while len(concat_product(n, 2)) <= 9:
        m = 2
        while len(concat_product(n, m)) <= 9:
            if is_pandigital(concat_product(n, m)):
                yield concat_product(n, m)
            m += 1
        n += 1


print(max(pandigital_concat_products()))
