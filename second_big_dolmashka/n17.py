with open(r'.\ioo\17_21903.txt') as file:
    data = [int(i) for i in file]

min_15 = min(i for i in data if abs(i) % 100 == 15 and 100 <= abs(i) <= 999)**2
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = (num1 * num2 * num3) > 0
    u2 = (min(i for i in (num1, num2, num3)) * max(i for i in (num1, num2, num3))) > min_15
    u3 = (min(i for i in (num1, num2, num3)) * max(i for i in (num1, num2, num3)))
    if u1 + u2 == 2:
        ans.append(u3)
print(min(ans))
