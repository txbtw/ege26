with open(r'.\files\17_6791.txt') as file:
    data = [int(i) for i in file]

ans = []
minn = min(i for i in data if abs(i) % 100 == 68)

for num1, num2 in zip(data, data[1:]):
    u = [1 for i in (num1, num2) if abs(i) % 100 == 68]
    u1 = abs(num1) % 100 == 68
    u2 = abs(num2) % 100 == 68
    f = (num1 ** 2 + num2 ** 2) >= minn
    quad = num1 ** 2 + num2 ** 2
    if (u1 + u2) ==  1 and f:
        ans.append(quad)
print(len(ans), max(ans))