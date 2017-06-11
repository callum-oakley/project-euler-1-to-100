import json

def value(word):
    return sum(ord(c) - ord("A") + 1 for c in word)

def filterTriangular(words):
    triangulars = {0}
    for word in words:
        while max(triangulars) < value(word):
            triangulars.add(max(triangulars) + len(triangulars))
        if value(word) in triangulars:
            yield word

def parse(fileName):
    return json.loads("[{}]".format(open(fileName).read().strip()))

print(len(list(filterTriangular(parse("data_042"))))) # 162
