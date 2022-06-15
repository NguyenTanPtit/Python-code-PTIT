# thống kê các từ khác nhau
import re
from collections import Counter

n = int(input())
s = ''
for i in range(n):
    s = s + " " + input().lower()
str1 = re.findall(r"\w+", s)
d = Counter(str1)
d = dict(sorted(d.items(), key=lambda x: (-x[1], x[0])))
for i in d:
    print(i, d[i])
