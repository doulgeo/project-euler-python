n0 = 0
n1 = 1
cond = True
fib = []
while cond == True:
    n = n0 + n1
    if n > 4000000:   #Check the condition
        cond = False
        break
    else:
        pass
    if n % 2 ==0 :   #Check if number is even
        fib.append(n)  #Adds Fibonacci number into list
    else:
        pass
    n0 = n1  #Change of variables to find the next number 
    n1 = n   #in sequence

total = 0
for num in fib:   #add the numbers in list to find the sum
    total = total + num

print total
