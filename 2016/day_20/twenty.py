with open('input.txt') as fd:
    data = fd.read()

def test_ip(n):
    for start, end in data:
        if start <= n <= end:
            break
    else:
        if n < 2**32:
            return True
    return False

data = sorted([int(x), int(y)] for x,y in [z.split('-') for z in data.splitlines()])

candidates = [x[1]+1 for x in data]

valids = [c for c in candidates if test_ip(c)]

total = 0
for ip in valids:
    while test_ip(ip):
        total += 1
        ip += 1


print(valids[0])
print(total)
