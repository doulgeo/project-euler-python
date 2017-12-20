"""PROBLEM 25:
Find the index of the first Fibonacci number to have 1000 digits
"""
import time


start = time.time()
def F():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

for index, fibonacci_number in enumerate(F()):
     length = len(str(fibonacci_number))
     if length == 1000:
         s = index
         break
end = time.time()
print ("The 1st Fibonacci number to have 1000 digits is the %sth and it took %s seconds") % (s,end-start)
