# tổng chữ số nguyên tố (thuận nghịch đã sửa)
import math


def sum(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum


def check(s):
    s1 = sum(s)
    if s1 < 2:
        return False
    for i in range(2, int(math.sqrt(s1))+1):
        if s1 % i == 0:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if check(n):
        print("YES")
    else:
        print("NO")
