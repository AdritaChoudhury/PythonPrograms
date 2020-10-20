import re
hand = open('sample.txt')
tot = 0
for line in hand:
    y = re.findall('[0-9]+',line)
    y = list(map(int, y))
    tot = tot + sum(y)
print(tot)
