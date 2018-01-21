from math import gcd

LIMIT = 12000

count = 0
for d in range(2, LIMIT + 1):
    n = d // 2
    while d < 3 * n:
        if gcd(n, d) == 1 and 2 * n < d:
            count += 1
        n -= 1
print(count)
