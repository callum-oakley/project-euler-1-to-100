def say(n):
    specialCases = {
        0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
        7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
        12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
        70: "seventy", 80: "eighty", 90: "ninety", 1000: "onethousand",
    }
    if n in specialCases:
        return specialCases[n]
    if n >= 100 and n % 100 == 0:
        return say(n // 100) + "hundred"
    if n >= 100 and n % 100 != 0:
        return say(n // 100) + "hundredand" + say(n % 100)
    # otherwise 10 < n < 100
    return say(10 * (n // 10)) + say(n % 10)

def sayAll(n):
    all = ""
    for words in (say(m + 1) for m in range(n)):
        all += words
    return all

# len(sayAll(1000)) == 21124
