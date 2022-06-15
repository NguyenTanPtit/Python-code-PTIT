# ngưỡng tối thiểu
from collections import Counter

s = input()
res = []
while len(s) >= 2:
    a = s[:2]
    res.append(a)
    s = s[2:]
res = Counter(res)
k = int(input())
a = []
check = False
for i in res:
    if res[i] >= k:
        a.append(i)
        check = True
if check:
    a.sort()
    for i in a:
        print(str(i)+" "+str(res[i]))
else:
    print('NOT FOUND')
