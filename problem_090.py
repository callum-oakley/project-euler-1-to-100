def subsets(xs, length):
    if length == 0:
        yield set()
    elif len(xs) == length:
        yield xs
    else:
        xs = xs.copy()
        x = xs.pop()
        yield from ({x} | ys for ys in subsets(xs, length - 1))
        yield from subsets(xs, length)


targets = [
    (6 if tens == 9 else tens, 6 if units == 9 else units)
    for tens, units in (divmod(n ** 2, 10) for n in range(1, 10))
]


def valid(dice1, dice2):
    return all(
        tens in dice1 and units in dice2 or tens in dice2 and units in dice1
        for tens, units in targets
    )


def main():
    dice = [{6 if f == 9 else f for f in d} for d in subsets(set(range(10)), 6)]

    count = 0
    for i in range(len(dice)):
        for j in range(i + 1):
            if valid(dice[i], dice[j]):
                count += 1

    return count
    # 1217
