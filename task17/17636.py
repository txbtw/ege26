with open(r'.\files\17_17636.txt') as file:
    data = [int(i) for i in file]
maxx = max(i for i in data if abs(i) % 3 == 0 and len(str(abs(i))) == 3)
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    cnt = [1 for i in (num1, num2, num3) if abs(i) % 10 == 3 and 100 <= abs(i) <= 999]
    if sum(cnt) >= 1 and (num1 + num2 + num3) < maxx:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))
