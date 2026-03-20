with open(r'.\files\17_11236.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if 1000 <= abs(i) <= 9999 and abs(i) % 10 == 1)
ans = []
min_2 = min(x for x in data if 10 <= abs(x) <= 99)**2
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    abss = abs(num1 * num2 * num3)
    u1 = num1 > min_2
    u2 = num2 > min_2
    u3 = num3 > min_2
    u4 = abss % maxx == 0
    if (u1 +u2 + u3) == 2 and u4 == 1:
        ans.append(sum(map(abs, [num1, num2,  num3])))
print(len(ans), max(ans))