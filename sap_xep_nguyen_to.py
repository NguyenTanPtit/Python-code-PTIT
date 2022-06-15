import math


def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


n = int(input())
s = list(map(int, input().split()))
ngto = []
res = []
for i in s:
    if check(i):
        ngto.append(i)
ngto.sort()
for i in s:
    if not check(i):
        res.append(i)
    else:
        res.append(ngto[0])
        ngto.remove(ngto[0])
for i in res:
    print(str(i), end=' ')
