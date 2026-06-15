with open(r'./files/17_28938.txt') as file:
    data = [int(i) for i in file]


max_28 = max(i for i in data if abs(i) % 100 == 28)
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = 100 <= abs(num1) <= 999
    u2 = 100 <= abs(num2)<= 999
    u3 = 100 <= abs(num3) <= 999
    f = (num1 + num2 + num3) / 3
    d = 0 < f < max_28
    if (u1 + u2 + u3) >= 1 and d:
        ans.append(num1 + num2 + num3)

print(len(ans), max(ans))