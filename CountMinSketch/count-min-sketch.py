import xxhash


class countMinSketch(object):
    stream = []

    m = 0
    k = 10
    t = 5
    Counters = []

    def __init__(self, path):
        with open(path, 'r') as file:
            for l in file: # Should only be one line, but just in case
                for char in l:
                    self.stream.append(char)
        self.m = len(self.stream)

    def initCounters(self):
        for i in range(self.t):
            self.Counters.append([])
            for j in range(self.k):
                self.Counters[i].append(0)


    def hashj(self, j, ai):
        """
        Returns a hash function of ai given j as the seed
        :param j: seed
        :param ai: item to hash
        :return: hash integer
        """
        h = xxhash.xxh32(seed=j)
        h.update(ai)
        hj = h.intdigest()%self.k
        return hj

    def countMinSketch(self):
        """
        Populates the counter table
        :return: nothing
        """
        self.initCounters()

        for i in range(self.m):
            for j in range(self.t):
                self.Counters[j][self.hashj(j, self.stream[i])] += 1

    def query(self, q):
        """
        Gets the frequency of the specified q
        :param q: the item to query
        :return: min frequency
        """
        m = self.Counters[0][self.hashj(0, q)]
        for j in range(self.t):
            current = self.Counters[j][self.hashj(j, q)]
            if m > current:
                m = current
        return m

path1 = '/Users/jesuszarate/SchoolSemesters/Spring2017/CS6140-DataMining/FrequentItems/S1.txt'
path2 = '/Users/jesuszarate/SchoolSemesters/Spring2017/CS6140-DataMining/FrequentItems/S2.txt'

cms1 = countMinSketch(path1)
cms1.countMinSketch()

print 'a - ' + str(cms1.query('a'))
print 'b - ' + str(cms1.query('b'))
print 'c - ' + str(cms1.query('c'))
print

# cms2 = countMinSketch(path2)
# cms2.countMinSketch()
#
# print 'a - ' + str(cms2.query('a'))
# print 'b - ' + str(cms2.query('b'))
# print 'c - ' + str(cms2.query('c'))

