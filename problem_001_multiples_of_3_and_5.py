# sum of every multiple of k from 0 to n inclusive
def closedSum(n, k):
    return k * (n // k) * (n // k + 1) // 2

print(closedSum(999, 3) + closedSum(999, 5) - closedSum(999, 15)) # 233168
