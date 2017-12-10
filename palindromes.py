"""PROBLEM 4:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

c = []
d = []
for x in range(111,1000):
    for y in range(111,1000):
        prod = str(x * y)
        for digit in prod:
            c.append(int(digit))
        if len(c) != 6:       #Digits must be an even number to have a palindrome.
            del c[:]          #Product of two 3-digist factors can't be more than 6 digits.
        elif (c[0] == c[5]) and (c[1] == c[4]) and (c[2] == c[3]):    #Checks in number is a palindrome
            d.append(prod)
print max(d)
