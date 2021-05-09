def main():
    n, total, step = 1, 1, 2
    while step <= 1000:
        for _ in range(4):
            n += step
            total += n
        step += 2
    return total
    # 669171001
