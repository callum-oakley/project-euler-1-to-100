def reverse(n):
    return int(''.join(reversed(str(n))))


def is_lychrel(n):
    for _ in range(49):
        n += reverse(n)
        if n == reverse(n):
            return False
    return True


print(sum(1 for n in range(10**4) if is_lychrel(n)))
