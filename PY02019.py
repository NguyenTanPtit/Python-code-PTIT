import math


def check(c, b):
    if math.gcd(c, b) == 1:
        return True
    else:
        return False


n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(0, n - 1):
    for j in range(i+1, n):
        if check(a[i], a[j]):
            print(str(a[i]) + " " + str(a[j]))
