from problem_004 import is_palindrome


def main():
    return sum(
        n for n in range(10 ** 6) if is_palindrome(str(n)) and is_palindrome(bin(n)[2:])
    )
    # 872187
