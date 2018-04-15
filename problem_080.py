from math import sqrt


def sqrt_expansion(n, length):
    n_scaled = n * 10 ** (2 * length - 2)
    upper = 10 ** length - 1
    lower = 10 ** (length - 1)
    last, mid = 0, 1
    while last != mid:
        last, mid = mid, (upper + lower) // 2
        if mid ** 2 < n_scaled:
            lower = mid
        elif mid ** 2 > n_scaled:
            upper = mid
    return str(mid)


def digital_sum(n):
    return sum(int(d) for d in n)


def is_square(n):
    return round(sqrt(n)) ** 2 == n


print(sum(digital_sum(sqrt_expansion(n, 100))
          for n in range(100)
          if not is_square(n)))
