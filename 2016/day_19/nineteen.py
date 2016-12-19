from time import time

data = 3017957

def josephus(n):
    bn = bin(n)[2:]
    return int(bn[1:]+bn[0], 2)

print(josephus(data))

class Item:
    def __init__(self, pos):
        self.pos = pos
        self.n = None
        self.p = None

    def steal(self):
        self.p.n = self.n
        self.n.p = self.p

def eliminate(n):
    circle = [Item(x) for x in xrange(n)]
    for elf in xrange(n):
        circle[elf].n = circle[(elf+1)%n]
        circle[elf].p = circle[(elf-1)%n]

    current = circle[0]
    mid = circle[n/2]

    for elf in xrange(n-1):
        mid.steal()
        mid = mid.n
        if (n-elf)%2 == 1:
            mid = mid.n
        current = current.n

    return current.pos+1

eliminate(data)
