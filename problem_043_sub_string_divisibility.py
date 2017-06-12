def isPandigitalish(s):
    return len({d for d in s}) == len(s)

def assemble(slices):
    return "".join(s[0] for s in slices) + slices[-1][1:]

def isValid(slices):
    return all(
        slices[i][1:] == slices[i + 1][:2]
        for i in range(len(slices) - 1)
    ) and isPandigitalish(assemble(slices))

def substringDivisiblePandigitals():
    divisors = [1, 2, 3, 5, 7, 11, 13, 17]
    slices = ["000" for _ in divisors]
    head = len(slices) - 1
    while head < len(slices):
        slices[head] = str(int(slices[head]) + divisors[head]).zfill(3)
        if len(slices[head]) > 3:
            slices[head] = "000"
            head += 1
        elif isValid(slices[head:]):
            if head == 0:
                yield assemble(slices)
            else:
                head -= 1

print(sum(int(s) for s in substringDivisiblePandigitals())) # 16695334890
