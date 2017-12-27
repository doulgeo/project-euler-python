"""PROBLEM 23:
A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown
that all integers greater than 28123 can be written as the
sum of two abundant numbers. However, this upper limit cannot be reduced
any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot
be written as the sum of two abundant numbers.

"""
import time
import math
st = time.time()

abundands = set()

#Function to compute the proper divisors of an integer
def Divs(n):
    divs = [1]
    for i in xrange(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])

    return sum(set(divs))

#Create a set of abundand numbers
for i in range(12,28124):
    if Divs(i)>i:
        abundands.add(i)


tot = set(i for i in range(1,28124)) #Generate Set of all numbers

#Remove numbers that can be written a sum of two abundand numbers.
for a in range(24,28124):
    for b in abundands:
        if b > a // 2: #Avoid a+b = b+a errors
            break
        if a-b in abundands:
            tot.remove(a)
            break


TotalSum = sum(tot) #The sum of numbers that cannot be written as a sum of two
                    #abundand numbers is the difference of the sum of all
                    #numbers minus the sum of the numbers that can be written
                    # as a sum of two abundand numbers.
en = time.time()
print "The sum is %s and it took %s seconds" % (TotalSum,en-st)
