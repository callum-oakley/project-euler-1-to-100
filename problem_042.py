from itertools import takewhile, count


def main():
    word_values = [
        sum(ord(c) - ord("A") + 1 for c in word)
        for word in eval(open("data/042").read())
    ]
    triangulars = (n * (n + 1) // 2 for n in count())
    ts = set(takewhile(lambda t: t < max(word_values), triangulars))
    return sum(1 for v in word_values if v in ts)
    # 162
