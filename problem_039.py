from problem_009 import pythagorean_triples


def main():
    solutions = {p: 0 for p in range(1001)}
    for t in pythagorean_triples(1001):
        solutions[sum(t)] += 1

    return max(solutions, key=solutions.get)
    # 840
