def isPandigital(s):
    return len({d for d in s} - {"0"}) == 9

def concatProduct(n, m):
    product = ""
    for m in range(1, m + 1):
        product += str(n * m)
    return product

def pandigitalConcatProducts():
    n = 1
    while len(concatProduct(n, 2)) <= 9:
        m = 2
        while len(concatProduct(n, m)) <= 9:
            if isPandigital(concatProduct(n, m)):
                yield concatProduct(n, m)
            m += 1
        n += 1

print(max(pandigitalConcatProducts()))
