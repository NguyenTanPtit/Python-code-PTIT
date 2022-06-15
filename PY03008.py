# đồ thi hình sao
res = {}
n = int(input())
for i in range(n-1):
    a, b = list(map(int, input().split()))
    if a in res:
        res[a] += 1
    else:
        res[a] = 1
    if b in res:
        res[b] += 1
    else:
        res[b] = 1
check = False
for i in res.keys():
    if res[i] == n - 1:
        check = True
        break
if check:
    print('Yes')
else:
    print('No')
