# bài toán tổ hợp
from itertools import combinations

n, k = list(map(int, input().split()))
s = list(map(int, input().split()))
s = set(s)
s = list(s)
s.sort()
k = list(combinations(s, k))
for i in k:
    for j in i:
        print(j, end=" ")
    print()
