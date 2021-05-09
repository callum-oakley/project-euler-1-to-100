from problem_021 import d


def main():
    abundants = list(n for n in range(1, 28124) if d(n) > n)
    abundant_sums = {a + b for a in abundants for b in abundants}
    return sum(set(range(1, 28124)) - abundant_sums)
    # 4179871
