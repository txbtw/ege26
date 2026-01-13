def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for x in range(10, 70001):
    num1 = 5**2025
    num2 = 5**400
    num = num1 + num2 - x
    convert(num, 5)

    ans.append(x)
print(max(ans))




