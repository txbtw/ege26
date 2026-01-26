ans = []
numx = 5*343**2031 + 4*49**2142 - 3*7**111 + 7**222
while numx:
    if numx % 7 != 0:
        ans.append(numx % 7)
    numx //= 7
print(sum(map(int, ans)))

