"""
The general idea is that each of the numbers that
have to divide the answer, can be assigned to a list of
bools. So if your test number is 2520, then if 11 divides it
then you have a true value appended in a list. If all 8 booleans
in this list are true then that means that every number divides the test.
"""

step = 2520

#start with 2520 as we know it is divided by range(1,10)
n = 2520 

c = [11,13,14,16,17,18,19,20] #only these numbers are neccessary
d = []
switch = 1

while switch == 1:
    for i in c:

        if not(n%i==0):  #first test if number is not divisable for speed
            break
        else:
            d.append(True)
        print d

    if all(d) and len(d) == 8: #len(d) must be 8 if every num. in c divides n
        print n
        switch = 0
        break
    else:
        del d[:]

    n = n + step
