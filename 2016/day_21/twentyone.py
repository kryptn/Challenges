from itertools import permutations

with open('input.txt') as fd:
    instructions = fd.read().splitlines()


class Parser:

    def __init__(self, seed, instructions):
        self.seed = list(seed)

        for ins in instructions:
            self.parse(ins)


    def swap_pos(self, x, y):
        self.seed[x], self.seed[y] = self.seed[y], self.seed[x]

    def swap_letters(self, a, b):
        ia = self.seed.index(a)
        ib = self.seed.index(b)
        self.swap_pos(ia, ib)

    def rotate(self, direction, dist):
        for x in xrange(dist):
            if direction > 0:
                self.seed = [self.seed[-1]]+self.seed[:-1]
            else:
                self.seed = self.seed[1:] + [self.seed[0]]


    def rotate_chr(self, c):
        ind = self.seed.index(c)
        if ind >= 4:
            ind += 1
        self.rotate(1, ind+1)
    
    def reverse(self, x, y):
        s = self.seed[:x]
        e = self.seed[y+1:]
        self.seed = s + list(reversed(self.seed[x:y+1])) + e
        pass

    def move(self, x, y):
        c = self.seed.pop(x)
        self.seed = self.seed[:y] + [c] + self.seed[y:]

    def parse(self, ins):
        lins = ins.split()
        if 'swap position' in ins:
            self.swap_pos(int(lins[2]), int(lins[5]))
        elif 'swap letter' in ins:
            self.swap_letters(lins[2], lins[5])
        elif 'rotate based' in ins:
            self.rotate_chr(lins[-1])
        elif 'rotate' in ins:
            self.rotate(-1 if lins[1] == 'left' else 1, int(lins[2]))
        elif 'reverse' in ins:
            self.reverse(int(lins[2]), int(lins[4]))
        elif 'move position' in ins:
            self.move(int(lins[2]), int(lins[5]))

p = Parser('abcdefgh', instructions)
print(''.join(p.seed))

end = 'fbgdceah'
for perm in permutations(end):
    p = Parser(perm, instructions)
    if ''.join(p.seed) == end:
        print(''.join(perm))
        break
    
