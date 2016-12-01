path = 'R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, R4, R4, R1, L5, L4, R5, R3, L1, R4, R3, L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, R2, R5, L3, R4, R76, L3, R4, R191, R5, R5, L5, L4, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, R4, R2, R3, R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, R3, R5, R2, R5, R5, L5, L5, R2, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, L4, L5, R3, L4, R1, R3, R2, R4, L2, L3, R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, R2, R1, L5, R5, R3, L3, L3, L2, R4, R2, L5, L1, L1, L5, L4, L1, L1, R1'

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
dirs = [Dirs(x) for x in path.split(', ')]

for d in dirs:
    grid.move(d)

print('star one: ', abs(grid.x) + abs(grid.y))
print('star two: ', sum(abs(x) for x in grid.visited_twice[0]))
