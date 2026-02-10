def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2


    i = 3
    while i * i < num:
        while num % i == 0:
            d +=[i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    return d
cnt = 0
for i in range(7_305_678, 10**20):
    d = fact(i)
    if len(d) == 4 and str(sum(d)) == str(sum(d))[::-1]:
        print(i, sum(d))
        cnt += 1
        if cnt == 5:
            break