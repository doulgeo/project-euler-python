count = 1
tot = 0
multis_of_fives = []
multis_of_threes = []

for i in range(1,1000):
    if i % 3 == 0 :

        tot = tot + i
        count = count + 1
        multis_of_threes.append(i)
        print "multiplier is", i
        print " current total =" , tot
    elif i % 5 == 0:

        tot = tot + i
        multis_of_fives.append(i)
        count = count + i
        print "multiplier is", i
        print " current total =" , tot
    else:
        pass
multis = multis_of_threes + multis_of_fives

print "Full total =" , tot
print len(multis)
print count
