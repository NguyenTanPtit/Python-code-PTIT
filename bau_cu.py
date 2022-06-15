from collections import Counter

a, b = list(map(int, input().split()))
s = list(map(int, input().split()))
s = Counter(s)
res = []
h = []
for i in s:
    res.append(s[i])
res.sort()
check = res[len(res)-1]
if res[0] == res[len(res)-1]:
    print('NONE')
else:
    x = len(res) - 1
    while check == res[x]:
        x -= 1
    check = res[x]
    for i in s:
        if s[i] == check:
            h.append(i)
    h.sort()
    print(str(h[0]))

