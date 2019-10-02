def adjacent_products(digits, n):
    for i in range(len(digits) - n + 1):
        product = 1
        for d in digits[i : i + n]:
            product *= int(d)
        yield product


def parse(file):
    return open(file).read().replace("\n", "")


print(max(adjacent_products(parse("data/008"), 13)))
