import random
import xxhash

path = '/Users/jesuszarate/SchoolSemesters/Spring2017/CS6140-DataMining/FrequentItems/S2.txt'

#a = [7,2,8,7,7,2,7,4,4,4,7]
stream = []
with open(path, 'r') as file:
    for l in file: # Should only be one line, but just in case
        for char in l:
            stream.append(char)

#stream = ['a','a','a','b','b','c','a','d','a','e','e','e','f',]
m = len(stream)
k = 10
t = 5
Counters = []

_memomask = {}

def hash_function(n):
    mask = _memomask.get(n)
    if mask is None:
        random.seed(n)
        mask = _memomask[n] = random.getrandbits(32)

    def myhash(x):
        return (hash(x) ^ mask)%k
    return myhash


def initCounters():
    for i in range(t):
        Counters.append([])
        for j in range(k):
            Counters[i].append(0)


def hashj(j, ai):
    h = xxhash.xxh32(seed=j)
    #h.update(stream[i])
    h.update(ai)
    hj = h.intdigest()%k
    return hj

def countMinSketch():
    initCounters()

    for i in range(m):
        for j in range(t):
            Counters[j][hashj(j, stream[i])] += 1

def query(q):
    #m = float('inf')
    m = Counters[0][hashj(0, q)]
    for j in range(t):
        # hj = hash_function(j)
        # current = Counters[j][hj(param)]
        current = Counters[j][hashj(j, q)]
        if m > current:
            m = current

        #m = min(m, current)
    return m

countMinSketch()

print 'a - ' + str(query('a'))
print 'b - ' + str(query('b'))
print 'c - ' + str(query('c'))

