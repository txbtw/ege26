import re




with open(r'../files/24_17641.txt') as file:
    data = file.readline()

num = r'([1-9][0-9]*|0)'

pattern = rf'({num}[+*])+{num}'

ma = [m.group() for m in re.finditer(pattern, data)]

ans = 0
for m in ma:
    if eval(m) == 0:
        ans = max(ans, len(m))
    elif len(m) > ans:
        for l in range(len(m) - 1):
            if m[l] in '*+': continue
            if m[l] == '0' and m[l + 1] not in '*+': continue
            for r in range(len(m) - 1, l, -1):
                if m[r] in '*+': continue
                new = m[l:r + 1]
                if new and eval(new) == 0:
                    ans = max(ans, len(new))
                    break

print(ans)