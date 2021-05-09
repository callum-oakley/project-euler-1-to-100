from problem_002 import fib


def main():
    n = 1
    while len(str(fib(n))) < 1000:
        n += 1
    return n
    # 4782
