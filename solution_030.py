def digitPowers(power):
    length = 2
    while length * 9 ** power >= 10 ** (length - 1):
        yield from (
            n for n in range(10 ** (length - 1), 10 ** length)
            if sum(int(d) ** power for d in str(n)) == n
        )
        length += 1

print(sum(digitPowers(5))) # 443839
