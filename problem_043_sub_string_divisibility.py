from math import factorial

def permute(xs, n):
    if len(xs) == 0:
        return xs
    granularity = factorial(len(xs) - 1)
    i = n // granularity
    return xs[i] + permute(xs[:i] + xs[i + 1:], n - i * granularity)

def permutations(s):
    return (permute(s, n) for n in range(factorial(len(s))))

def isSubStringDivisible(s):
    return all([
        int(s[1:4]) % 2 == 0,
        int(s[2:5]) % 3 == 0,
        int(s[3:6]) % 5 == 0,
        int(s[4:7]) % 7 == 0,
        int(s[5:8]) % 11 == 0,
        int(s[6:9]) % 13 == 0,
        int(s[7:10]) % 17 == 0
    ])

print(sum(
    int(p) for p in permutations("0123456789")
    if isSubStringDivisible(p)
)) # 16695334890
