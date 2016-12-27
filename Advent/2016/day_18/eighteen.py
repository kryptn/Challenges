data = '^.....^.^^^^^.^..^^.^.......^^..^^^..^^^^..^.^^.^.^....^^...^^.^^.^...^^.^^^^..^^.....^.^...^.^.^^.^'

def chunks(iterable, n):
    for index, _ in enumerate(iterable[:-n+1]):
        yield iterable[index:index+n]

def eval(triple):
    l,c,r = triple
    if (l != c and c == r) or (l == c and c != r):
        return '^'
    return '.'

def detect(row):
    return ''.join(eval(ch) for ch in chunks('.'+row+'.', 3))

def detect_rows(seed, dist):
    safes = seed.count('.')
    for x in xrange(dist-1):
        seed = detect(seed)
        safes += seed.count('.')

    print(safes)

detect_rows(data, 40)
detect_rows(data, 400000)
