with open('data/three/input.txt') as fd:
    data = [[int(x) for x in sorted(y.split())] for y in fd.read().splitlines()]

def check(a, b, c):
    if a+b > c:
        if a+c > b:
            if c+b > a:
                return True
    return False


print(len([x for x in data if check(*x)]))
