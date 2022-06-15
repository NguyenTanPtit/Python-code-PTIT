# từ điển
from collections import Counter

t = int(input())
str1 = ""
while t > 0:
    t -= 1
    str1 += input() + " "
s = list(map(str, str1.split()))
s.sort()
res = Counter(s)
res = dict(sorted(res.items(), reverse=True, key=lambda x: x[1]))
for i in res:
    print(i + " " + str(format("%.2f" % (res[i] / len(s)))))
