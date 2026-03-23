with open(r'.\files\17_9840.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if 1000 <= abs(i) <= 9999 and abs(i) % 100 == 39)**2
ans = []
for num1, num2 in zip(data, data[1:]):
    cnt = [1 for i in (num1, num2) if len(str(abs(i))) == 4]
    if sum(cnt) == 1 and (num1 + num2)**2 <= maxx:
        ans.append(num1 + num2)
print(len(ans), max(ans))