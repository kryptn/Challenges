from collections import Counter

with open('input.txt') as fd:
    data = fd.read()

data_counted = [Counter(x).most_common() for x in zip(*data.splitlines())]

print('first star: {}'.format(''.join(x[0][0] for x in data_counted)))
print('second star: {}'.format(''.join(x[-1][0] for x in data_counted)))

