from problem_015 import choose


def main():
    return sum(1 for n in range(101) for r in range(n + 1) if choose(n, r) > 10 ** 6)
    # 4075
