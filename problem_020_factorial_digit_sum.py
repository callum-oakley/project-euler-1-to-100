from math import factorial

def digitSum(n):
    return sum(int(d) for d in str(n))

# digitSum(factorial(100)) == 648
