with open(r'./files/17_29971.txt') as file:
    data = [int(i) for i in file]


max_33 = max(x for x in data if abs(x) % 100 == 33)

ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = 10 <= abs(num1) <= 99
    u2 = 10 <= abs(num2) <= 99
    u3 = 10 <= abs(num3) <= 99
    f = (num1 + num2 + num3) ** 2 < max_33
    if (u1 + u2 + u3) == 2 and f:
        ans.append(num1 + num2 + num3)

print(len(ans), max(ans))