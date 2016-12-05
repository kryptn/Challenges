class Dirs:
    def __init__(self, dir):
        self.direction = dir[0]
        self.distance = int(dir[1:])

    def __repr__(self):
        return '<{}: {}>'.format(self.direction, self.distance)

class Grid:

    #             west     north   east    south
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = 1 # Assume initial direction north
        self.visited = [(0,0)] # we start at 0,0
        self.visited_twice = []

    def move(self, dir):
        turn = 1 if dir.direction  == 'R' else -1
        self.dir = (self.dir + turn) % 4
        vx, vy = self.directions[self.dir]

        for x in range(dir.distance):
            self.x += vx
            self.y += vy
            pos = (self.x, self.y)
            self.visited.append(pos)

            if self.visited.count(pos) == 2:
                self.visited_twice.append(pos)

grid = Grid()
with open('input.txt') as fd:
    dirs = [Dirs(x) for x in fd.read().split(', ')]

for d in dirs:
    grid.move(d)

print('star one: ', abs(grid.x) + abs(grid.y))
print('star two: ', sum(abs(x) for x in grid.visited_twice[0]))
