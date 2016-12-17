from hashlib import md5
from collections import OrderedDict

seed = 'edjrjqaa'

class Coord:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __nonzero__(self):
        if not self.x and not self.y:
            return False
        return True

    def __repr__(self):
        return '<{}, {}>'.format(self.x, self.y)

class Rooms:

    dirs = OrderedDict()
    dirs['U'] = Coord(0, 1)
    dirs['D'] = Coord(0,-1)
    dirs['L'] = Coord(-1,0)
    dirs['R'] = Coord(1, 0)

    def __init__(self, seed, h=4, w=4, pos=(0,4)):
        self.seed = seed
        self.paths = []
        self.pos = Coord(0,3)
        self.goal = Coord(3,0)
        self.height = h
        self.width = w

    def validate(self, pos, coord, ch):
        t = pos+coord
        if ch in 'bcdef':
            if 0 <= t.y < self.height:
                if 0 <= t.x < self.width:
                    return True
        return False

    def look(self, pos, path):
        candidate = md5(self.seed+path).hexdigest()[:4]
        iterator = zip(self.dirs.items(), candidate)
        return [x[0] for x in iterator if self.validate(pos, x[0][1], x[1])]

    def move(self, pos, path=''):
        if pos == self.goal:
            self.paths.append(path)
            return
        doors = self.look(pos, path)
        for d in doors:
            self.move(pos+d[1], path+d[0])

r = Rooms(seed)
r.move(r.pos)
sr = sorted(r.paths, key=len)
print(sr[0])
print(len(sr[-1]))
