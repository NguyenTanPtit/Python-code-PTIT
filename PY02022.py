import math
from collections import Counter


def check(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
s = input().split()
res = Counter(s)
for i in res:
    if check(int(i)):
        print(f"{i} {res[i]}")
