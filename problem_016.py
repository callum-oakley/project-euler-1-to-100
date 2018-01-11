def digitSum(n):
    return sum(int(d) for d in str(n))

print(digitSum(2 ** 1000))
