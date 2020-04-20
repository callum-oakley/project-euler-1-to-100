LIMIT = 10 ** 6 + 1


d = {n: 0 for n in range(1, LIMIT)}
for n in range(1, LIMIT):
    for k in range(2 * n, LIMIT, n):
        d[k] += n


loops = {}

visited = set()
for n in range(1, LIMIT):
    chain = [n]
    visited.add(n)
    m = d[n]
    while m > 0 and m < LIMIT and m not in chain and m not in visited:
        chain.append(m)
        visited.add(m)
        m = d[m]
    if m in chain:
        loop = chain[chain.index(m) :]
        loops[min(loop)] = len(loop)

print(max(loops, key=lambda k: loops[k]))
