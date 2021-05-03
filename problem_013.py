def parse(file):
    return [int(l) for l in open(file).read().splitlines()]


print(str(sum(parse("data/013")))[:10])
# 5537376230
