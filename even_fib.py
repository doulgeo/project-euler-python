n0 = 0
n1 = 1
cond = True
fib = []
while cond == True:
    n = n0 + n1
    if n > 4000000:
        cond = False
        break
    else:
        pass
    if n % 2 ==0 :
        fib.append(n)
    else:
        pass
    n0 = n1
    n1 = n

total = 0
for num in fib:
    total = total + num

print total
