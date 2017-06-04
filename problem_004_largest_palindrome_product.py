def isPalindrome(x):
    return x == x[::-1]

def largestPalindromeProduct(ns):
    return max(x * y for x in ns for y in ns if isPalindrome(str(x * y)))

# largestPalindromeProduct(range(100, 1000)) = 906609
