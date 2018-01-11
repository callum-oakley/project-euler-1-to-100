def champernowne():
    n = 0
    while True:
        yield from str(n)
        n += 1

def charsAt(s, indices):
    for i, d in enumerate(s):
        if i > max(indices):
            break
        if i in indices:
            yield d

product = 1
for d in charsAt(champernowne(), {10 ** i for i in range(7)}):
    product *= int(d)

print(product)
