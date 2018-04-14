def is_palindrome(x):
    return x == x[::-1]


ns = range(100, 1000)
print(max(x * y for x in ns for y in ns if is_palindrome(str(x * y))))
