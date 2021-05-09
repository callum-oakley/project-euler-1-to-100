from problem_007 import primes


def main():
    pl = list(primes(10 ** 6))
    ps = set(pl)
    longest = []
    for i in range(len(pl)):
        j = i + len(longest) + 1
        while j < len(pl) and sum(pl[i:j]) < 10 ** 6:
            if sum(pl[i:j]) in ps:
                longest = pl[i:j]
            j += 1
    return sum(longest)
    # 997651
