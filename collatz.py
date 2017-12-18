"""PROBLEM 14:
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5-> 16-> 8-> 4-> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time

seq_len = 0

def collatz(n):
    global seq_len
    while n>1:
        if n%2==1:
            n = (3*n+1)/2
            seq_len += 1
        else:
            n = n/2
            seq_len += 1
    return seq_len


start = time.time()

maxlen = 0
maxnum = 0

for i in range(2,1000000):
    seq_len = 0
    collatz(i)
    if seq_len>maxlen:
        maxlen = seq_len
        maxnum = i



time= time.time()
tim = time -start

print "The steps of the collatz sequence is", maxlen, "for number %s and time:%s" % (maxnum,tim)
