def isPalindrome(s):
    return all(s[i] == s[-i - 1] for i in range(len(s) // 2))

def isDoubleBasePalindrome(n):
    return isPalindrome(str(n)) and isPalindrome(bin(n)[2:])

print(sum(n for n in range(10 ** 6) if isDoubleBasePalindrome(n)))
