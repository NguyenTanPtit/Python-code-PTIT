# thống kê các từ khác nhau theo ngưỡng k
import re
from collections import Counter

n, k = list(map(int, input().split()))
s = ""
for i in range(n):
    s = s + " " + input().lower()
s1 = re.findall(r"\w+", s)
d = Counter(s1)
d = dict(sorted(d.items(), key=lambda x: (-x[1], x[0])))
for i in d:
    if d[i] >= k:
        print(i, d[i])
