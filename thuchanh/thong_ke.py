import re
from typing import Counter

n = int(input())
res = ''
for i in range(n):
    res += " " + input().lower()
res = re.findall(r'\w+', res)
s = Counter(res)
s = dict(sorted(s.items(), key=lambda a: (-a[1], a[0])))
for i in s:
    print(i, s[i])
