with open('input.txt') as fd:
    data = fd.read()

def test_ip(n):
    for start, end in data:
        if start <= n <= end:
            break
    else:
        return True
    return False


data = sorted([int(x), int(y)] for x,y in [z.split('-') for z in data.splitlines()])

candidates = [x[1]+1 for x in data]

valids = [c for c in candidates if test_ip(c)]

total = 0
for ip in valids:
    repeat = True
    while repeat:
        if test_ip(ip) and ip < 4294967296:
            total += 1
            ip += 1
        else:
            repeat = False

print(valids[0])
print(total)
