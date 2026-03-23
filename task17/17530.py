with open(r'.\files\17_17530.txt') as file:
    data = [int(i) for i in file]
ans = []
minn = min(i for i in data)
for num1, num2 in zip(data, data[1:]):
    u1 = num1 % 55 == minn
    u2 = num2 % 55 == minn
    if u1 + u2 >= 1:
        ans.append(num1 + num2)
print(len(ans), min(ans))