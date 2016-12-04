
from collections import Counter

with open('data/four/input.txt') as fd:
    data = fd.read().splitlines()

test = 'aaaaa-bbb-z-y-x-123[abxyz]'

def truth(enc):
    elements = enc.split('-')
    sector, checksum = elements[-1][:-1].split('[')
    counter = Counter(''.join(elements[:-1]))
    tcs = sorted( sorted(counter.keys()), key=lambda x: counter[x], reverse=True)
    if checksum == ''.join(tcs[:5]):
        return int(sector)
    return 0

true_data = [x for x in data if truth(x)]

print('star one: {} '.format(sum(truth(x) for x in true_data))


