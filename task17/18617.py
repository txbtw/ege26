with open(r'.\files\17_18617 (1).txt') as file:
    data = [int(i) for i in file]
maxx = max(i for i in data)
minn = min(i for i in data)
ans = []
for nums in zip(data, data[1:]):
    u1 = [x % 3 == maxx % 3 for x in nums]
    u2 = [x % 7 == minn % 7  for x in nums]
    if sum(u1) >= 1 and sum(u2) >= 1:
        ans.append(sum(nums))
print(len(ans), max(ans))


