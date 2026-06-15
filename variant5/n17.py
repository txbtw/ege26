with open(r'./files/17_21903.txt') as file:
    data = [int(i) for i in file]

minn_15 = min(x for x in data if abs(x) % 100 == 15 and 100 <= abs(x) <= 999) ** 2

for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = 