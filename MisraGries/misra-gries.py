import random

#path = '/Users/jesuszarate/SchoolSemesters/Spring2017/CS6140-DataMining/FrequentItems/S1.txt'
path = '/Users/jesuszarate/SchoolSemesters/Spring2017/CS6140-DataMining/FrequentItems/S2.txt'

#a = [7,2,8,7,7,2,7,4,4,4,7]
a = []
with open(path, 'r') as file:
    for l in file: # Should only be one line, but just in case
        for char in l:
            a.append(char)

k = 10

counters = []
labels = []
d = {}
length = k - 1

sub = 0



def subtractFromAll():
    for l, c in d.items():
        if c == 1:
            d.pop(l)
        else:
            d[l] -= 1


for i in range(0, len(a)):
    if a[i] in d:
        d[a[i]] += 1
    else:
        if len(d) < length:
            d[a[i]] = 1
        else:
            subtractFromAll()
            sub += 1

print d

for l, c in d.items():
    print l + " , " + str(float(c)/1000000.0),
print

count = 0
for c in a:
    if c == 'a':
        count += 1


print "count = " + str(count)
