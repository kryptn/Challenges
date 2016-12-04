
from collections import Counter, namedtuple
from string import ascii_lowercase as alpha

with open('data/four/input.txt') as fd:
    data = fd.read().splitlines()

test = 'aaaaa-bbb-z-y-x-123[abxyz]'

Room = namedtuple('Room', ('name', 'sector'))

def word_shift(word, offset):
    return ''.join( alpha[ (alpha.index(c)+offset)%26 ] for c in word)

def shift(words, offset):
    return ' '.join(word_shift(word, offset) for word in words)

def truth(enc):
    elements = enc.split('-')
    sector, checksum = elements[-1][:-1].split('[')
    counter = Counter(''.join(elements[:-1]))
    tcs = sorted( sorted(counter.keys()), key=lambda x: counter[x], reverse=True)
    if checksum == ''.join(tcs[:5]):
        return Room(shift(elements[:-1], int(sector)), int(sector))
    return None


# filter out fake rooms
true_data = list(filter(lambda x: x, [truth(x) for x in data]))

# sum of real room sectors
print('star one: {}'.format( sum(x.sector for x in true_data) ))

# find north pole object storage
print('star two: {}'.format( list(filter(lambda x: 'northpole' in x.name, true_data))[0].sector))



