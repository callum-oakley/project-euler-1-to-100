from math import gcd

def simplify(a_b):
    a, b = a_b
    return (a // gcd(a, b), b // gcd(a, b))

def cancelDigit(a_b, d):
    a, b = a_b
    return (int(str(a).replace(d, "", 1)), int(str(b).replace(d, "", 1)))

digitCancellingFractions = (
    (a, b) for b in range(11, 100) for a in range(10, b)
    if a % 10 != 0 and b % 10 != 0
    for commonDigit in {d for d in str(a) if d in str(b)}
    if simplify(cancelDigit((a, b), commonDigit)) == simplify((a, b))
)

productA, productB = 1, 1
for a, b in digitCancellingFractions:
    productA, productB = productA * a, productB * b

print(simplify((productA, productB))[1]) # 100
