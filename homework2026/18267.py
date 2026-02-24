def f(start, end):
    if start == end: return 1
    if start > end: return 0
    if start == 6:
        return f(start + 2, end) + f(start + 5, end)
    return f(start + 2, end) + f(start + 5, end) + f(start ** 2, end)

print(f(4, 36))


####################

def f(start, end, last):
    if start == end and last != 'c': return 1
    if start > end: return 0
    return f(start + 2, end, 'a') + f(start + 5, end, 'b') + f(start ** 2, end,'c')

print(f(4, 36, ''))


