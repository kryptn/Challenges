from hashlib import md5
from itertools import count
import re

pat = re.compile(r'(.)\1\1')

data = 'cuanljph'

def mhash(d, i, stretch=False):
    if stretch:
        f = mhash(d, i)
        for x in xrange(2016):
            f = md5(f).hexdigest()
        return f
    return md5(d+str(i)).hexdigest()

def otp(seed, stretch=False):
    counter = count()
    hashes = []
    pattern = re.compile(r'(.)\1\1')

    c = counter.next()
    while len(hashes) < 64:
        result = pattern.findall(mhash(seed, c, stretch))
        if result:
            print('hash found? {}'.format(c))
            for x in xrange(c+1, c+1000):
                if result[0]*5 in mhash(data, x, stretch):
                    print('\t\t\tFound!')
                    hashes.append(c)
        c = counter.next()

    return hashes

r = otp(data)

print(r[-1])
            
r = otp(data, True)

print(r[-1])

