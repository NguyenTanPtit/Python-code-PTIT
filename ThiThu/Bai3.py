# danh sach username
t = int(input())
res = []
while t > 0:
    t -= 1
    s = input().lower()
    if s in res:
        continue
    else:
        res.append(s)
for i in res:
    print(i)
