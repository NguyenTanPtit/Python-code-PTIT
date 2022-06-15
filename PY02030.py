# phân chia nguyên tố
import math


def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


t = int(input())
s = list(map(int, input().split()))
res = []
k = False
for i in s:
    if i not in res:
        res.append(i)
for i in range(len(res)):
    sums = 0
    sumi = 0
    for j in range(i + 1, len(res)):
        sums += res[j]
    for n in range(0, i+1):
        sumi += res[n]
    if check(sumi) and check(sums):
        print(str(i))
        k = True
        break
if not k:
    print('NOT FOUND')

