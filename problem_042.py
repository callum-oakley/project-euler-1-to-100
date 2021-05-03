import json


def value(word):
    return sum(ord(c) - ord("A") + 1 for c in word)


def filter_triangular(words):
    triangulars = {0}
    for word in words:
        while max(triangulars) < value(word):
            triangulars.add(max(triangulars) + len(triangulars))
        if value(word) in triangulars:
            yield word


def parse(file):
    return json.loads("[{}]".format(open(file).read().strip()))


print(len(list(filter_triangular(parse("data/042")))))
# 162
