from itertools import izip, cycle

data =  [ [False if x is not 1 else True for x in range(13)],
          [False if x is not 10 else True for x in range(19)],
          [False if x is not 2 else True for x in range(3)],
          [False if x is not 1 else True for x in range(7)],
          [False if x is not 3 else True for x in range(5)],
          [False if x is not 5 else True for x in range(17)] ]

test = [[False, False, False, False, True],[False,True]]

def stagger(disks):
    return [disk[index:]+disk[:index] for index, disk in enumerate(disks)]

def spin(disks):

    for index, alignment in enumerate( izip(*[cycle(x) for x in stagger(disks)])):
        if all(alignment):
            print(index+1)
            break

def d1(t): return (t+1) % 13 == 0
def d2(t): return (t+10) % 19 == 0
def d3(t): return (t+2) % 3 == 0
def d4(t): return (t+1) % 7 == 0
def d5(t): return (t+3) % 5 == 0
def d6(t): return (t+5) % 17 == 0
def d7(t): return (t) % 11 == 0

n = 0
while True:
    if all((d1(n+1), d2(n+2), d3(n+3), d4(n+4), d5(n+5), d6(n+6))):
        print(n)
        break
    n += 1



n = 0
while True:
    if all((d1(n+1), d2(n+2), d3(n+3), d4(n+4), d5(n+5), d6(n+6), d7(n+7))):
        print(n)
        break
    n += 1
