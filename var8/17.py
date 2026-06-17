with open(r'17_17611.txt') as file:
    data = [int(i) for i in file]

max_7 = max(x for x in data if abs(x) % 10 == 7 and 1000 <= abs(x) <= 9999)

ans = []
for num1, num2, num3 in zip(data, data[1:],data[2:]):
    u1 = 1000 <= abs(num1) <= 9999 and abs(num1) % 10 == 7
    u2 = 1000 <= abs(num2) <= 9999 and abs(num2) % 10 == 7
    u3 = 1000 <= abs(num3) <= 9999 and abs(num3) % 10 == 7
    f = (num1 + num2 + num3) > max_7
    if (u1 + u2 + u3) >= 2 and f:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))