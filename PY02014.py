# biến đổi nguyên tố
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
step = 0
for i in s:
    if not check(i):
        for j in range(1, i):
            if check(i + j):
                step = max(step, j)
                break
            if check(i - j):
                step = max(step, j)
                break
print(step)
