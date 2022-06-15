# EMIRP NUMBER
import math


def check(n):
    prime = [True for _ in range(n + 1)]
    prime[0] = False
    prime[1] = False
    i = 2
    while i * i <= n:
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
        i += 1
    return prime


t = int(input())
num = 1000001
prime = check(num)
while t:
    t -= 1
    n = int(input())
    res = []
    for i in range(13, n):
        y = int(str(i)[::-1])
        if prime[i] and prime[y] and i != y and y < n and i not in res:
            res.append(i)
            res.append(y)
    print(*res)
