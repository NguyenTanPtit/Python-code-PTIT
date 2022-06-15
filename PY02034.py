# đếm các số có 2 chữ số
from collections import Counter

s = input()
res = []
while len(s) >= 2:
    a = s[:2]
    res.append(a)
    s = s[2:]
res = Counter(res)
for i in res:
    print(str(i)+" "+str(res[i]))
