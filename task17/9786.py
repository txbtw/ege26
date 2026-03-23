with open(r'.\files\17_9786.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if abs(i) % 100 == 25)
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    cnt = [1 for num in (num1, num2, num3) if len(str(abs(num))) == 4]
    if sum(cnt) <= 2 and (num1 + num2 + num3) <= maxx:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))