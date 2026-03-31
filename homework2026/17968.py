with open(r'.\files\17968.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for line in data:
    line = sorted(line)
    if line[-1] < sum(line) - line[-1]:
