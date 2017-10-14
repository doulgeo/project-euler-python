import time



def euler(n):
    i = 2        #First prime number relevant in multiplication
    ans = 1
    pfactors = []
    cond = True
    while cond == True:
        if i > n:   #Checks if possible divisor is greater
            cond = False  #than our divident
        else:
            pass

        if n % i == 0:   
            pfactors.append(i)
            n = n / i #Makes sure that i is a prime number
            i = 2
            print
        else:
            i = i + 1


    print pfactors

start_time = time.time()
exec_time = time.time() - start_time
print "time is: ", float(exec_time)
