import math


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def checkLen(n):
    s = str(n)
    if prime(len(s)):
        return True
    else:
        return False


def checkQuantity(n):
    s = str(n)
    countPrime = 0
    count1 = 0
    for i in s:
        if prime(int(i)):
            countPrime += 1
        else:
            count1 += 1
    if countPrime > count1:
        return True
    return False


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if checkQuantity(n) and checkLen(n):
        print("YES")
    else:
        print("NO")
