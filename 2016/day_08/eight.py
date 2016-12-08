with open('input.txt') as fd:
    data = fd.read()

class Screen:
    def __init__(self):
        self.grid = [[False]*50 for x in range(6)]
    
    def shift_row(self, row, spaces):
        self.grid[row] = self.grid[row][-spaces:]+self.grid[row][:-spaces]

    def shift_col(self, col, spaces):
        self.grid = zip(*self.grid)
        self.shift_row(col, spaces)
        self.grid = [list(x) for x in zip(*self.grid)]

    def enable(self, length, height):
        for x in range(length):
            for y in range(height):
                self.grid[y][x] = True


    def __str__(self):
        return '\n'.join(' '.join('#' if x else '.' for x in row) for row in self.grid)

    def parse(self, inp):
        i = inp.split()
        if i[0] == 'rect':
            x, y = i[1].split('x')
            self.enable(int(x), int(y))
        else:
            shift = self.shift_row if i[1] == 'row' else self.shift_col
            col = int(i[2].split('=')[1])
            mag = int(i[4])
            shift(col, mag)

s = Screen()
for d in data.splitlines():
    s.parse(d)

print('star one: {}\nstar two:\n'.format(sum(sum(x) for x in s.grid)))
print(s)

