import time



def euler(n):
    i = 2
    ans = 1
    pfactors = []
    cond = True
    while cond == True:
        if i > n:
            cond = False
        else:
            pass

        if n % i == 0:
            pfactors.append(i)
            n = n / i
            i = 2
            print
        else:
            i = i + 1


    print pfactors
start_time = time.time()
euler(600851475143)

wra = time.time() - start_time
print "time is: ", float(wra)
