with open(r'.\files\17_23902 (1).txt') as file:
    data = [int(i) for i in file]
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u = [str(x)[0] == str(x)[-1] for x in (num1, num2, num3)]
    f = [1000 <= i <= 9999 and str(i)[1] == '2' for i in (num1, num2, num3)]
    if sum(u) == 1 and sum(f) == 2:
        ans.append(max(num1, num2, num3))

print(len(ans), sum(ans))