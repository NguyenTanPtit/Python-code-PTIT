# số có 9 ước
# N = x^2 sao cho x =a*b với a, b nguyên tố. VD: 36, 100, ...
import math


def check(n):
    s = n
    res = []
    for i in range(2, int(math.sqrt(s)) + 1):
        while s % i == 0:
            res.append(i)
            s /= i
    if s > 2:
        res.append(s)
    res2 = set(res)
    if len(res2) == 2 and len(res) == 2:
        return True
    elif len(res2) == 1 and len(res) == 4:
        return True
    return False


t = int(input())
dem = 0
for i in range(6, int(math.sqrt(t))+1):
    if check(i):
        dem += 1
print(dem)
