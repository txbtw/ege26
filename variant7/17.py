with open(r'./files/17_21712.txt') as file:
    data = [int(i) for i in file]

minn = min(x for x in data if x > 0 and 1000 <= abs(x) <= 9999 and abs(x) % 10 == 6)
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = 1000 <= abs(num1) <= 9999 and abs(num1) % 10 == 6
    u2 = 1000 <= abs(num2) <= 9999 and abs(num2) % 10 == 6
    u3 = 1000 <= abs(num3) <= 9999 and abs(num3) % 10 == 6
    f = (num1 + num2 + num3) <= minn
    if (u1 + u2 + u3) == 1 and f:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))
