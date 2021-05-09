def main():
    names = sorted(eval(open("data/022").read()))
    return sum(
        i * sum(ord(c) - ord("A") + 1 for c in name) for i, name in enumerate(names, 1)
    )
    # 871198282
