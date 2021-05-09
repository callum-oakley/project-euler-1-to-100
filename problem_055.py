from problem_004 import is_palindrome


def is_lychrel(n):
    for _ in range(49):
        n += int("".join(reversed(str(n))))
        if is_palindrome(str(n)):
            return False
    return True


def main():
    return sum(1 for n in range(10 ** 4) if is_lychrel(n))
    # 249
