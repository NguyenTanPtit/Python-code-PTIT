# liệt kê các số có 2 chữ số tăng dần
s = input()
res = []
while len(s) >= 2:
    a = s[:2]
    res.append(a)
    s = s[2:]
res = set(res)
res = list(res)
res.sort()
for i in res:
    print(i, end=' ')
