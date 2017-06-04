def adjacentProducts(digits, n):
    for i in range(len(digits) - n + 1):
        product = 1
        for d in digits[i:i + n]:
            product *= int(d)
        yield product

def parse(fileName):
    return open(fileName).read().replace("\n", "")

print(max(adjacentProducts(parse("data_008"), 13))) # 23514624000
