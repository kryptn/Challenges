from itertools import izip_longest

with open('data/three/input.txt') as fd:
    data = [[int(x) for x in y.split()] for y in fd.read().splitlines()]



def check(a, b, c):
    if a+b > c:
        if a+c > b:
            if c+b > a:
                return True
    return False

def twisted(d):
    args = [iter(d)] * 3
    nd = list(izip_longest(*args))
    zd = list(zip(*x) for x in nd)
    return [x for y in zd for x in y]


print(len([x for x in data if check(*x)]))
print(len([x for x in twisted(data) if check(*x)]))

