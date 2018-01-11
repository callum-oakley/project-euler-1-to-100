from math import factorial

def digitSum(n):
    return sum(int(d) for d in str(n))

print(digitSum(factorial(100)))
