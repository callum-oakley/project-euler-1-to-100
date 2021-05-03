def champernowne():
    n = 0
    while True:
        yield from str(n)
        n += 1


def chars_at(s, indices):
    for i, d in enumerate(s):
        if i > max(indices):
            break
        if i in indices:
            yield d


product = 1
for d in chars_at(champernowne(), {10 ** i for i in range(7)}):
    product *= int(d)

print(product)
# 210
