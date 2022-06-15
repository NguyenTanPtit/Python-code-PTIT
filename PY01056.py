# CHẴN – LẺ - NGUYÊN TỐ
import math


def checkChan(n):
    s = str(n)
    for i in range(0, len(s), 2):
        if int(s[i]) % 2 != 0:
            return False
    return True


def checkLe(n):
    s = str(n)
    for i in range(1, len(s), 2):
        if int(s[i]) % 2 == 0:
            return False
    return True


def sum(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum


def prime(n):
    s = sum(n)
    if s < 2:
        return False
    for i in range(2, int(math.sqrt(s))+1):
        if s % i == 0:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if checkLe(n) and checkChan(n) and prime(n):
        print("YES")
    else:
        print("NO")
