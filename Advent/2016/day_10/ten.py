from collections import defaultdict, namedtuple, deque

with open('input.txt') as fd:
    data = fd.read()

Instruction = namedtuple('Instruction', ('high', 'low'))
Action = namedtuple('Action', ('value', 'dest'))

class Bot:
    
    def __init__(self):
        self.ins = deque()
        self.chips = []
        self.compared = []
        self.output = False

    def give(self, chip):
        self.chips.append(chip)

    def ins_add(self, ins):
        self.ins.appendleft(ins)

    @property
    def high(self):
        return sorted(self.chips)[-1]

    @property
    def low(self):
        return sorted(self.chips)[0]

    def __call__(self, chip=None, ins=None):
        if chip:
            print('\tAdding {}'.format(chip))
            self.give(chip)

        if ins:
            print('\tAdding {}'.format(ins))
            self.ins_add(ins)

        if not self.output and len(self.chips) == 2 and len(self.ins):
            ins = self.ins.pop()
            print('\t\tcomparing {} and {}'.format(self.low, self.high))
            r = [Action(self.high, ins.high), Action(self.low, ins.low)]
            self.compared.append((self.low, self.high))
            self.chips = []
            return r
        return None


class Tray:

    def __init__(self, instructions):
        self.tray = defaultdict(Bot)
        self.queue = deque()
        self.instructions = instructions
        
    def work(self, instructions=None):
        if instructions:
            self.instructions = instructions
        
        for ins in self.instructions:
            self.parse(ins)
            while self.queue:
                self.do(self.queue.pop())

    def parse(self, ins):
        ins = [int(x) if x.isdigit() else x for x in ins.split()]
        if 'gives' in ins:
            low = ins[6] if ins[5] == 'bot' else ins[6]+1000
            high = ins[11] if ins[10] == 'bot' else ins[11]+1000
            dest = ins[1]
            
            instruction = Instruction(high, low)
            print('giving bot {} {}'.format(dest, instruction))
            result = self.tray[dest](ins=instruction)
            self.validate(result)
        else:
            self.queue.appendleft(Action(ins[1], ins[-1]))

    def do(self, action):
        if action.value >= 1000:
            self.tray[action.dest].output = True

        print('giving bot {} {}'.format(action.dest, action))
        result = self.tray[action.dest](chip=action.value)
        self.validate(result)

    def validate(self, result):
        if result:
            for action in result:
                self.queue.appendleft(action)


t = Tray(data.splitlines())
t.work()
r = [k for k, v in t.tray.items() if (17,61) in v.compared][0]
print('star one: {}'.format(r))
print('star two: {}'.format(t.tray[1000].chips[0] * t.tray[1001].chips[0] * t.tray[1002].chips[0]))
