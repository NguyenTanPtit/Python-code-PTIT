import math


def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def sums(n):
    sum = 0
    s = str(n)
    for i in s:
        sum += int(i)
    return sum


n = int(input())
while n > 0:
    n -= 1
    a, b = list(map(int, input().split()))
    if check(sums(math.gcd(a, b))):
        print("YES")
    else:
        print("NO")
