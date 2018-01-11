def parse(fileName):
    return [int(l) for l in open(fileName).read().splitlines()]

print(str(sum(parse("data/013")))[:10])
