with open(r'./files/17_27629.txt') as file:
    data = [int(i) for i in file]


maxx = max(x for x in data if 1000 <=abs(x) <= 9999 and abs(x) % 100 == 43) ** 2
ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = 1000 <= abs(num1) <= 9999
    u2 = 1000 <= abs(num2) <= 9999
    f = (num1 + num2) ** 2
    d = f < maxx
    if (u1 + u2) >= 1 and d:
        ans.append(f)

print(len(ans), max(ans))