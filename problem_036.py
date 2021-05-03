def is_palindrome(s):
    return all(s[i] == s[-i - 1] for i in range(len(s) // 2))


def is_double_base_palindrome(n):
    return is_palindrome(str(n)) and is_palindrome(bin(n)[2:])


print(sum(n for n in range(10 ** 6) if is_double_base_palindrome(n)))
# 872187
