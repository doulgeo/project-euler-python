"""PROBLEM 22:
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each
name, multiply this value by its alphabetical position in
the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
 So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

import time
start_time = time.time()
text_file = open("p022_names.txt", "r")
lines = text_file.read().split(',') #Turn .txt file to list

lines = sorted(lines)
mylst = map(lambda each:each.strip('"'), lines) #remove " to save time
mylst = list(mylst) #convert map object to list to make it iterable

alphabet = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,
            'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,
            'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
tsum = 0
for name in mylst:
    parsum = 0
    i = mylst.index(name) + 1 #Cautious of python zero-indexing!!

    for letter in name:

        
        if letter in alphabet:
            parsum = parsum + alphabet[letter]
    parsum = parsum * i
    tsum = parsum + tsum
end_time = time.time()
exec_time = end_time - start_time
print "Answer is %s and it took %s seconds" % (tsum,exec_time)
>>>>>>> 0cf951df6bfb42e635d8b59d2b2d5f1bdd8e7708
