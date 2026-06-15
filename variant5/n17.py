with open(r'./files/17_21903.txt') as file:
    data = [int(i) for i in file]

minn_15 = min(x for x in data if abs(x) % 100 == 15 and 100 <= abs(x) <= 999) ** 2
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = num1 > 0 and num2 > 0 and num3 > 0
    u2 = num1 < 0 and num2 < 0 and num3 < 0
    mi = min(num1, num2, num3)
    ma = max(num1, num2, num3)
    f = ma * mi
    d = f > minn_15
    if (u1 + u2) == 1 and d:
        ans.append(f)
print(len(ans), min(ans))
