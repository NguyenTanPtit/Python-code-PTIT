import math


def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = list(map(int, input().split()))
t = 2
print(n[1], end=' ')
count = 1
while True:
    if count == n[0]+1:
        break
    if check(t):
        n[1] += t
        print(n[1], end=' ')
        count += 1
    t += 1
