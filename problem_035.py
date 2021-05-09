from problem_007 import primes


def rotations(s):
    return (s[i:] + s[:i] for i in range(1, len(s)))


def main():
    ps = set(primes(10 ** 6))
    count = 0
    for p in ps:
        if all(int(r) in ps for r in rotations(str(p))):
            count += 1
    return count
    # 55
