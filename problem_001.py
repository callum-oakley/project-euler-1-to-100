# sum of every multiple of k from 0 to n inclusive
def closed_sum(n, k):
    return k * (n // k) * (n // k + 1) // 2


print(closed_sum(999, 3) + closed_sum(999, 5) - closed_sum(999, 15))
# 233168
