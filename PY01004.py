import math


def check(a, b):
    if math.gcd(a, b) == 1:
        return True
    else:
        return False


def prime(a):
    if a < 2: return False
    for i in range(2, int(math.sqrt(a)) + 1, 1):
        if a % i == 0:
            return False
    return True


t = int(input())
while t > 0:
    n = int(input())
    count = 0
    for i in range(1, n):
        if check(i, n):
            count += 1
    if prime(count):
        print('YES')
    else:
        print('NO')
    t -= 1
