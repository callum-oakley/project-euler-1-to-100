from functools import cache


@cache
def relevant(pos):
    x, y = pos
    return (
        {(x, j) for j in range(9)}
        | {(i, y) for i in range(9)}
        | {(x // 3 * 3 + i, y // 3 * 3 + j) for j in range(3) for i in range(3)}
    )


class Sudoku:
    def __init__(self, vals):
        self.grid = {}
        self.legal = {
            (x, y): set(range(1, 10)) for y in range(9) for x in range(9)
        }
        for y in range(9):
            for x in range(9):
                if (val := next(vals)) != 0:
                    self.set((x, y), val)

    def __str__(self):
        return (
            "\n".join(
                " ".join(
                    str(self.grid[(x, y)]) if (x, y) in self.grid else "\u00b7"
                    for x in range(9)
                )
                for y in range(9)
            )
            + "\n"
        )

    def set(self, pos, val):
        self.grid[pos] = val
        for r in relevant(pos):
            self.legal[r].discard(val)

    def unset(self, pos):
        del self.grid[pos]
        for r in relevant(pos):
            self.legal[r] = set(range(1, 10)) - {
                self.grid[q] for q in relevant(r) if q in self.grid
            }

    def solutions(self):
        empty = {
            (x, y)
            for y in range(9)
            for x in range(9)
            if (x, y) not in self.grid
        }
        if len(empty) > 0:
            pos = min(empty, key=lambda pos: len(self.legal[pos]))
            for guess in self.legal[pos].copy():
                self.set(pos, guess)
                yield from self.solutions()
                self.unset(pos)
        else:
            yield self

    def solve(self):
        return next(self.solutions())


def parse(file):
    lines = open(file).readlines()
    return [
        Sudoku(int(d) for line in lines[i : i + 9] for d in line.strip())
        for i in range(1, len(lines), 10)
    ]


def main():
    return sum(
        100 * solved.grid[(0, 0)]
        + 10 * solved.grid[(1, 0)]
        + solved.grid[(2, 0)]
        for solved in (s.solve() for s in parse("data/096"))
    )
    # 24702
