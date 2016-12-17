seed = 'edjrjqaa'


class Rooms:

    def __init__(self, seed):
        self.seed = seed
        self.paths = []
        self.pos = (0,3)
        self.goal = (3,0)

    def move(self, path, pos):
    
