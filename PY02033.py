# liệt kê các số có 2 chữ số theo thứ tự xuất hiện
s = input()
res = []
while len(s) >= 2:
    a = s[:2]
    if a not in res:
        res.append(a)
    s = s[2:]
for i in res:
    print(i, end=' ')
