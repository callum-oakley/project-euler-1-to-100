from math import ceil, sqrt


def is_prime(n):
    if n <= 1:
        return False
    for divisor in range(2, ceil(sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True


total = 13
prime = 8
side_len = 7
while prime / total >= 0.1:
    side_len += 2
    total += 4
    for k in range(1, 4):
        prime += 1 if is_prime(side_len ** 2 - k * (side_len - 1)) else 0
print(side_len)
