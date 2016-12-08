

with open('input.txt') as fd:
    data = fd.read().splitlines()

def abba(s):
    if s == s[::-1] and s[0] != s[1]:
        return True
    return False

def chunks(iterable, n):
    for index, _ in enumerate(iterable[:-n+1]):
        yield iterable[index:index+n]

def parse(ips):
    split_ip = ips.replace('[', ' ').replace(']', ' ').split()
    return split_ip[::2], split_ip[1:][::2]

def verify_TLS(ip):
    n, h = parse(ip)
    if any(any(abba(x) for x in chunks(y, 4)) for y in n):
        if not any(any(abba(x) for x in chunks(y, 4)) for y in h):
            return True
    return False

def verify_SSL(ip):
    supernet, hypernet = parse(ip)
    flip = lambda s: s[1]+s[0]+s[1]
    superchunks = [x for y in [chunks(z, 3) for z in supernet] for x in y]
    hyperchunks = [x for y in [chunks(z, 3) for z in hypernet] for x in y]

    abas = [chunk for chunk in superchunks if abba(chunk)]

    return set([flip(x) for x in abas]).intersection(set(hyperchunks))

tls = [verify_TLS(x) for x in data]
ssl = [True if verify_SSL(x) else False for x in data]

print('star one: {}'.format(sum(tls)))
print('star two: {}'.format(sum(ssl)))
