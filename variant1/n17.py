with open(r'./files/17_23376.txt') as file:
    data = [int(i) for i in file]

maxx_37 = max(i for i in data if 10000 <= abs(i) <= 99999 and abs(i) % 100 == 37) ** 2
ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = 10000 <= abs(num1) <= 99999
    u2 = 10000 <= abs(num2) <= 99999
    u3 = (num1 **2 + num2 ** 2) > maxx_37
    if (u1 + u2) == 1 and u3:
        ans.append(num1 + num2)

print(len(ans), max(ans))
