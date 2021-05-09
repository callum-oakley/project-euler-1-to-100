from problem_032 import is_pandigital


def concat_product(n, m):
    product = ""
    for m in range(1, m + 1):
        product += str(n * m)
    return product


def pandigital_concat_products():
    n = 1
    while len(concat_product(n, 2)) <= 9:
        m = 2
        while len(p := concat_product(n, m)) <= 9:
            if is_pandigital(p):
                yield p
            m += 1
        n += 1


def main():
    return max(pandigital_concat_products())
    # 932718654
