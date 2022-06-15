# chữ số nguyên tố
import math


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def checkLen(n):
    s = str(n)
    if prime(len(s)):
        return True
    return False


def checkPrime(n):
    countPr = 0
    countNotPr = 0
    s = str(n)
    for i in s:
        if prime(int(i)):
            countPr += 1
        else:
            countNotPr += 1
    if countPr > countNotPr:
        return True
    return False


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if checkPrime(n) and checkLen(n):
        print('YES')
    else:
        print('NO')
