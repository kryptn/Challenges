

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

def verify_ip(ip):
    n, h = parse(ip)
    if any(any(abba(x) for x in chunks(y, 4)) for y in n):
        if not any(any(abba(x) for x in chunks(y, 4)) for y in h):
            return True
    return False

r = [verify_ip(x) for x in data]

print('star one: {}'.format(sum(r)))
