from itertools import permutations, count


def try_eval(s):
    try:
        yield eval(s)
    except ZeroDivisionError:
        return


def possibilities(abcd):
    for op1 in ("+", "-", "*", "/"):
        for op2 in ("+", "-", "*", "/"):
            for op3 in ("+", "-", "*", "/"):
                for a, b, c, d in permutations(abcd):
                    yield from try_eval(f"(({a}{op1}{b}){op2}{c}){op3}{d}")
                    yield from try_eval(f"{a}{op1}({b}{op2}({c}{op3}{d}))")
                    yield from try_eval(f"({a}{op1}({b}{op2}{c})){op3}{d}")
                    yield from try_eval(f"{a}{op1}(({b}{op2}{c}){op3}{d})")
                    yield from try_eval(f"({a}{op1}{b}){op2}({c}{op3}{d})")


def first_missing(ns):
    ns = set(ns)
    return next(n for n in count(1) if n not in ns)


def main():
    a, b, c, d = max(
        (
            (a, b, c, d)
            for d in range(4, 10)
            for c in range(3, d)
            for b in range(2, c)
            for a in range(1, b)
        ),
        key=lambda abcd: first_missing(possibilities(abcd)),
    )

    return f"{a}{b}{c}{d}"
    # 1258
