with open(r'.\files\17_12249.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if i % 10 == 3 and 10000 <= abs(i) <= 99999)
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = num1 % 10 == 3
    u2 = num2 % 10 == 3
    u3 = num3 % 10 == 3
    summ3 = num1 + num2 + num3
    if u1 + u2 + u3 >= 1 and summ3 <= maxx:
       ans.append(num1 + num2 + num3)
print(len(ans), max(ans))