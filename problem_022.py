import json


def parse(file):
    return json.loads("[{}]".format(open(file).read().strip()))


def score(names):
    return sum(
        i * sum(ord(c) - ord("A") + 1 for c in name)
        for i, name in enumerate(names, 1)
    )


print(score(sorted(parse("data/022"))))
# 871198282
