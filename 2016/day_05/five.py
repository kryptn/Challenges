from hashlib import md5
from itertools import count

def check(code):
    hashed = md5(code).hexdigest()

    if hashed.startswith('00000'):
        return hashed[5], hashed[6]
    return None

def basic(hashed, password):
    password += hashed[0]
    return password

def adv(hashed, password):
    pos, c = hashed
    if pos.isdigit() and int(pos) < 8 and pos not in password:
        password[pos] = c
    return password

def finish(pw):
    return ''.join(v for k,v in sorted(pw.items(), key=lambda x: x[0]))

def crack(seed, method, pass_obj, handler=None):
    counter = count()
    password = pass_obj()

    while len(password) < 8:
        r = check(seed+str(counter.next()))
        if r:
            password = method(r, password)

    if handler:
        return handler(password)

    return password

data = 'ojvtpuvg'

# crack(data, basic, str)

# crack(data, adv, dict, finish)

