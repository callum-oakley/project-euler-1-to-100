def isPandigital(s):
    return len({d for d in s} - {"0"}) == 9

def areSufficientlySmall(a, b):
    # If the expression for the product of a and b contains more than 9 digits,
    # then a and b can't possibly form a pandigital product.
    return len(str(a) + str(b) + str(a * b)) < 10

def pandigitalProducts():
    a, b = 1, 2
    # We assume throughout that a < b. If a and a + 1 are not sufficiently
    # small, then a, b won't be sufficiently small for any b.
    while areSufficientlySmall(a, a + 1):
        # Likewise, if a and b are not sufficently small, then a, b' won't be
        # sufficiently small for any b' > b.
        while areSufficientlySmall(a, b):
            if isPandigital(str(a) + str(b) + str(a * b)):
                yield a * b
            b += 1
        a, b = a + 1, a + 2

print(sum(set(pandigitalProducts()))) # 45228
