import math


def prime(a, b):
    if math.gcd(a, b) == 1:
        return True
    return False


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    s = int(str(n)[::-1])
    if prime(n,s):
        print("YES")
    else:
        print("NO")


