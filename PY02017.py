# tần suất lẻ
from collections import Counter

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    s = list(map(int, input().split()))
    d = Counter(s)
    for i in d:
        if d[i] % 2 != 0:
            print(i)
