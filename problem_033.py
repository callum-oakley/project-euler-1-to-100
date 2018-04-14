from math import gcd


def simplify(a_b):
    a, b = a_b
    return (a // gcd(a, b), b // gcd(a, b))


def cancel_digit(a_b, d):
    a, b = a_b
    return (int(str(a).replace(d, "", 1)), int(str(b).replace(d, "", 1)))


digit_cancelling_fractions = (
    (a, b) for b in range(11, 100) for a in range(10, b)
    if a % 10 != 0 and b % 10 != 0
    for common_digit in {d for d in str(a) if d in str(b)}
    if simplify(cancel_digit((a, b), common_digit)) == simplify((a, b)))

product_a, product_b = 1, 1
for a, b in digit_cancelling_fractions:
    product_a, product_b = product_a * a, product_b * b

print(simplify((product_a, product_b))[1])
