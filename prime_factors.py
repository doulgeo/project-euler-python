"""PROBLEM 3:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import time

def euler(n):
    i = 2        #First prime number relevant in multiplication
    ans = 1
    pfactors = []

    while True:
        if i > n:  #Checks if possible divisor is greater
              break  #than our divident
        elif n % i == 0:
            pfactors.append(i)
            n = n / i #Makes sure that i is a prime number
            i = 2
            print
        else:
            i = i + 1


    return max(pfactors)

start_time = time.time()
print euler( 600851475143)
exec_time = time.time() - start_time
print "time is: ", float(exec_time)
