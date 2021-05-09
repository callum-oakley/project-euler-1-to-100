def digit_sum(n):
    return sum(int(d) for d in str(n))


def main():
    return digit_sum(2 ** 1000)
    # 1366
