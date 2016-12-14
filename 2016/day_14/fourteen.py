from hashlib import md5
from itertools import count
from collections import deque, namedtuple
import re

pat = re.compile(r'(.)\1\1')

data = 'cuanljph'

IndexedHash = namedtuple('IndexedHash', ('index', 'hash'))

class Hashes:

    pattern = re.compile(r'(.)\1\1')
    roll = 2016

    def __init__(self, seed, super_secure=False):
        self.seed = seed
        self.super_secure = super_secure
        self.hashes = deque()
        self.results = []
        self.init_hashes()

        self.run()

    def hack(self, index):
        h = md5(self.seed+str(index)).hexdigest()
        if self.super_secure:
            for _ in xrange(self.roll):
                h = md5(h).hexdigest()
        self.hashes.append(IndexedHash(index, h))

    def init_hashes(self):
        for index in xrange(1000):
            self.hack(index)
        self.latest = index

    def cycle(self):
        self.hack(self.hashes[-1].index+1)
        return self.hashes.popleft()

    def check(self):
        h = self.cycle()
        r = self.pattern.findall(h.hash)
        if r:
            if any(r[0]*5 in x.hash for x in self.hashes):
                self.results.append(h)

    def run(self):

        while len(self.results) < 64:
            self.check()

        print(self.hashes[-1].index)

h = Hashes(data)
hs = Hashes(data, True)






