def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for x in range(1, 2401):
    num1 = convert(7*9**210 + 6*9**110 - x, 9)
    if num1.count('0') == 100:
        print(int(x))
# ans = 2394


