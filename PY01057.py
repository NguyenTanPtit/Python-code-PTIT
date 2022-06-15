# vị trí nguyên tố
import math


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    s = str(n)
    check = True
    for i in range(len(s)):
        if prime(i):
            if not prime(int(s[i])):
                check = False
                break
        else:
            if prime(int(s[i])):
                check = False
                break
    if check:
        print("YES")
    else:
        print("NO")



