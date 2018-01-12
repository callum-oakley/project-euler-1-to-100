def infRange(n=0, step=1):
    while True:
        yield n
        n += step

def search(multiples):
    for x in infRange(1):
        if len({tuple(sorted(str(k * x))) for k in multiples}) == 1:
            return x

print(search([1, 2, 3, 4, 5, 6]))
