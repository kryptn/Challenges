with open('input.txt') as fd:
    data = fd.read().strip()

def v2(s, do_v2=False):
    total = 0
 
    while s:
        if s[0] != '(':
            total += 1
            s = s[1:]
            continue

        n = s.find(')')

        length, repeat = [int(x) for x in s[1:n].split('x')]

        if do_v2:
            total += v2(s[n+1: n+1+length], True) * repeat
        else:
            total += length * repeat

        s = s[n+1+length:]

    return total


print('star one: {}'.format(v2(data)))
print('star two: {}'.format(v2(data, True)))
