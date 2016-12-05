from hashlib import md5
from itertools import count


#with open('input.txt') as fd:
#    data = fd.read()

data = 'ojvtpuvg'

def check(code):
    hashed = md5(code).hexdigest()

    if hashed.startswith('00000'):
        return hashed[5], hashed[6]
    return None

def crack_basic(seed):
    counter = count()
    password = ''
    while len(password) < 8:
        r = check(seed+str(counter.next()))
        if not r:
            continue
        password += r[0]

    return password

def crack_adv(seed):
    counter = count()
    password = {}
    while len(password) < 8:
        r = check(seed+str(counter.next()))
        if not r:
            continue
        pos, c = r
        if pos.isdigit() and int(pos) < 8 and pos not in password:
            password[pos] = c

    return ''.join(v for k,v in sorted(password.items(), key=lambda x: x[0]))




def v2(seed):

    password = {}
    def check(inp):
        h = md5(inp).hexdigest()
        if h.startswith('00000'):
            print(inp)
            pos = h[5]
            c = h[6]
            if pos.isdigit() and int(pos) < 8:
                print('\t Passed')
                return pos, c
            print('\t Failed')
        return None
    counter = count(0)

    while len(password) < 8:
        r = check(seed+str(counter.next()))
        if r:
            pos, c = r
            if pos not in password:
                password[pos] = c

    print(''.join(v for k,v in sorted(password.items(), key=lambda x: x[0])))

# v1(data)

# v2(data)

