data = 3017957

def josephus(n):
    bn = bin(n)[2:]
    return int(bn[1:]+bn[0], 2)

print(josephus(data))


