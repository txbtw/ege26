with open(r'.\files\17.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if 10 <= i <= 99)
ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = 10 <= num1 <= 99
    u2 = 10 <= num2 <= 99
    u3 = (num1 + num2) % maxx == 0
    if (u1 + u2) == 1 and u3:
        ans.append(num1 + num2)
print(len(ans), max(ans))