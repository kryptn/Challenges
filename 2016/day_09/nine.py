with open('input.txt') as fd:
    data = fd.read()

def expand(s):
    if s[0] == '(':
        n = s.find(')')
        dist, repeat = s[1:n].split('x')
        return s[n+1:n+1+int(dist)] * int(repeat), s[n+int(dist)+1:]
    else:
        return s[0], s[1:]

def decompress(s):
    final = ''

    while s:
        f, s = expand(s)
        final += f

    return final

print('star one: {}'.format(len(decompress(data))))
