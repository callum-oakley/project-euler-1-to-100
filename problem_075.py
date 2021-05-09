from problem_009 import pythagorean_triples


def main():
    solutions = {p: 0 for p in range(1500001)}
    for t in pythagorean_triples(1500001):
        solutions[sum(t)] += 1

    return sum(1 for c in solutions.values() if c == 1)
    # 161667
