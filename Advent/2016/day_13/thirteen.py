from pathing.path import AStar

data = 1362

class Bunny(AStar):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.aoc_input = kwargs.get('aoc')
        self.dest=self[1][1]
        

    def makewalls(self):
        for x in range(len(self.keys())):
            for y in range(len(self[0].keys())):
                self.formula(x, y)

    def formula(self, x, y):
        r = (x*x) + (3*x) + (2*x*y) + y + (y*y) + self.aoc_input
        self[x][y].fr = r
        br = str(bin(r))
        self[x][y].br = br
        if br.count('1')%2:
            self[x][y].passable=False

b = Bunny(60,60,aoc=data, dest=(1,1))
b.makewalls()
b.path()
print('star one: {}'.format(b[31][39].distance))
rawcells = [x for y in [z.values() for z in b.values()] for x in y]
valid = [x for x in rawcells if 0 < x.distance <= 50]
print('star two: {}'.format(len(valid)))
