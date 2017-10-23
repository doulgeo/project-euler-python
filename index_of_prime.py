def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True




def index(n):

    c = []
    i = 2

    while len(c) < n:

        if isPrime(i) :
            c.append(i)
        else:
            pass
        i += 1
    print c[n-1]
