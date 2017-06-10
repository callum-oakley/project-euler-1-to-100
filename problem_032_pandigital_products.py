def isPandigital(s):
    return len({d for d in s} - {"0"}) == 9

def pandigitalProducts():
    a, b = 1, 1
    while len(str(a ** 2)) + 2 * len(str(a)) < 10:
        while len(str(a * b)) + len(str(a)) + len(str(b)) < 10:
            if isPandigital(str(a) + str(b) + str(a * b)):
                yield a * b
            b += 1
        a, b = a + 1, a + 2

print(sum(set(pandigitalProducts()))) # 45228
