def special_triplet(n):
    # Assume a <= b <= c and a + b + c == n
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if c >= b and a ** 2 + b ** 2 == c ** 2:
                return (a, b, c)

a, b, c = special_triplet(1000)
print(a * b * c)
