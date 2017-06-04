def parse(fileName):
    return [int(l) for l in open(fileName).read().splitlines()]

print(str(sum(parse("data_013")))[:10]) # 5537376230
