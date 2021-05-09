def is_palindrome(x):
    return x == x[::-1]


def main():
    return max(
        x * y
        for x in range(100, 1000)
        for y in range(x, 1000)
        if is_palindrome(str(x * y))
    )
    # 906609
