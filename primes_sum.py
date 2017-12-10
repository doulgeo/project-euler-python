"""PROBLEM 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time

start_time = time.time()

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True

def primes(limit):

    total = 0
    for i in range(1,limit):
        if isPrime(i):
            total = total + i
    return total

print primes(2000000)
end = time.time()
print end - start_time
