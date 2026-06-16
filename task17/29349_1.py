with open(r'./files/17_29349.txt') as file:
    data = [int(i) for i in file]


min_123  = min(x for x in data if x > 0 and x % 123 == 0)
ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = (num1 + num2) < min_123
    if u1:
        ans.append(num1 + num2)

print(len(ans), max(ans))