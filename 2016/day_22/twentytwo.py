from collections import defaultdict

with open('input.txt') as fd:
    data = fd.read()

class Node:
    def __init__(self, line):
        l = line.split()
        x,y = [int(x[1:]) for x in l[0].split('-')[-2:]]
        self.x = x
        self.y = y
        self.size = int(l[1][:-1])
        self.used = int(l[2][:-1])
        self.avail = int(l[3][:-1])

        if self.used == 0:
            self.disp = '_'
        elif self.size > 500:
            self.disp = 'X'
        elif self.x == 0 and self.y == 26:
            self.disp = 'G'
        elif self.x == self.y == 0:
            self.disp = 'T'
        else:
            self.disp = '.'

    def fits(self, node):
        if self.avail >= node.used:
            return True
        return False

    def __str__(self):
        return self.disp

def square(iterable):
    for x in iterable:
        for y in iterable:
            yield x, y

def valid(x, y):
    if x is not y:
        if x.used > 0 and x.used <= y.avail:
            return True
    return False

def print_grid(ns):
    for x in xrange(0,27*27,27):
        print(''.join(str(n) for n in ns[x:x+27]))

nodes = [Node(x) for x in data.splitlines()]
viable = [pair for pair in square(nodes) if valid(*pair)]
print(len(viable))
