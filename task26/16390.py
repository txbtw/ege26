with open(r'.\files\26_16390.txt') as file:
    s, n = map(int, file.readline().split())
    boxes = [int(i) for i in file]


boxes = sorted(boxes)
ans = []
for box in boxes:
    if sum(ans) + box <= s:
        ans += [box]

free_space = s - sum(ans[:-1])

print(len(ans), max(i for i in boxes if i <= free_space))


