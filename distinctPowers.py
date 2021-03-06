"""PROBLEM 29:
Consider all integer combinations of a^b for 2 <= a <= 5 and 2 <= b <= 5:
f they are then placed in numerical order, with any repeats removed,
we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence
generated by a^b for 2 <= a <= 100 and 2 <= b <= 100?
"""
#Using sets because they are sequences without duplicates
s = set()
for a in range(2,101):
    for b in range(2,101):
        s.add(a**b)

print len(s)
