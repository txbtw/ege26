with open(r'.\files\17_25356.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if i % 100 == 30)
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = not(1000 <= abs(num1) <= 9999)
    u2 = len(str(abs(num2))) != 4
    u3 = not(1000 <= abs(num3) <= 9999)
    if u1 + u2 + u3 == 3 and (num1 + num2 + num3 ) > maxx:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))
