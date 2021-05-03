def rings(partial, unused):
    if not magic(partial):
        return
    if len(partial) % 3 == 0 or len(partial) % 3 == 2 or len(partial) == 1:
        if len(unused) == 0:
            yield partial + [partial[1]]
        for n in unused:
            if len(partial) == 0 or len(partial) % 3 != 0 or n > partial[0]:
                yield from rings(partial + [n], unused - {n})
    else:
        yield from rings(partial + [partial[-2]], unused)


def magic(ring):
    return (
        len(
            set(
                sum(ring[3 * j + i] for i in range(3))
                for j in range(len(ring) // 3)
            )
        )
        <= 1
    )


rs = ("".join(str(d) for d in r) for r in rings([], set(range(1, 11))))
print(max(r for r in rs if len(r) == 16))
# 6531031914842725
