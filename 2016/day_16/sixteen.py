seed = '01110110101001000'
reqlen = 272
reqlen2 = 35651584

def dragon(s):
    r = ''.join('0' if x == '1' else '1' for x in reversed(s))
    return '{}0{}'.format(s, r)

def inflate(seed, length):
    while len(seed) < length:
        seed = dragon(seed)

    return seed[:length]

def pairs(i):
    while i:
        yield next(i)+next(i)

def checksum(s):
    return ''.join('1' if x[0] == x[1] else '0' for x in pairs(iter(s)))

def reduce_cs(s):
    while not len(s) % 2:
        s = checksum(s)
    return s


print('star one: {}'.format(reduce_cs(inflate(seed, reqlen))))
print('star one: {}'.format(reduce_cs(inflate(seed, reqlen2))))
