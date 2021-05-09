def main():
    power, total, length = 5, 0, 2
    while length * 9 ** power >= 10 ** (length - 1):
        for n in range(10 ** (length - 1), 10 ** length):
            if sum(int(d) ** power for d in str(n)) == n:
                total += n
        length += 1
    return total
    # 443839
