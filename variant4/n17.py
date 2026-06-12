with open(r'./files/17_17558.txt') as file:
    data = [int(i) for i in file]

mod32 = sum(abs(x) % 32 == 0 for x in data)
ans = []

for num1, num2 in zip(data, data[1:]):
    u1 = num1 < 0
    u2 = num2 < 0
    f = (num1 + num2) < mod32
    if (u1 + u2) >= 1 and f:
        ans.append(num1 + num2)
print(len(ans), max(ans))