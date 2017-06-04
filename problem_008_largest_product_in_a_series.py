from functools import reduce
from operator import mul

def adjacentProducts(digits, n):
    for i in range(len(digits) - n + 1):
        yield reduce(mul, (int(d) for d in digits[i:i + n]), 1)

def parse(fileName):
    return open(fileName).read().replace("\n", "")

# max(adjacentProducts(parse("data_008"), 13)) == 23514624000
