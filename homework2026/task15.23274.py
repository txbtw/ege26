def f(x, y):
    return (2 * x + y != 110) or (x < y) or (a < x)
ans = []
for a in range(0, 1000)[::-1]:
    if all(f(x,y) for x in range(0, 1000) for y in range(0, 1000)):
        ans.append(a)
print(max(ans))
