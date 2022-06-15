import math


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    n = input()
    s = int(n[len(n)-4:])
    if prime(s):
        print("YES")
    else:
        print("NO")
