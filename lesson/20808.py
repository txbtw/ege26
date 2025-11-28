ans = []
for x in range(1, 2031):
    cnt0 = 0
    num = 7 ** 170 + 7 ** 100 - x
    while num:
        if num % 7 == 0:
            cnt0 += 1
        num //= 7
    ans.append([x, cnt0])
print(max(ans))





