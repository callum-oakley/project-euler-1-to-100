def is_pandigitalish(s):
    return len({d for d in s}) == len(s)


def assemble(slices):
    return "".join(slice[0] for slice in slices) + slices[-1][1:]


def is_valid(slices):
    return all(
        slices[i][1:] == slices[i + 1][:2] for i in range(len(slices) - 1)
    ) and is_pandigitalish(assemble(slices))


def substring_divisible_pandigitals():
    divisors = [1, 2, 3, 5, 7, 11, 13, 17]
    # Since we know each 3 digit slice is divisible by each of the above in
    # turn, we can search the space of possible slices, which turns out to be
    # way faster than searching the space of 0-9-pandigitals.
    slices, head = ["000" for _ in divisors], len(divisors) - 1
    while head < len(slices):
        slices[head] = str(int(slices[head]) + divisors[head]).zfill(3)
        if len(slices[head]) > 3:
            slices[head], head = "000", head + 1
        elif head == 0 and is_valid(slices):
            yield assemble(slices)
        elif is_valid(slices[head:]):
            head -= 1


print(sum(int(s) for s in substring_divisible_pandigitals()))
# 16695334890
