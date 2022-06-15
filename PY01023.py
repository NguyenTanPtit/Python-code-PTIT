import math


def prime(n):
    print('1 ', end="")
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count = 0
            while n % i == 0:
                n /= i
                count += 1
            print('* ' + str(i) + '^' + str(count) + ' ', end="")
    if n > 2:
        print("* " + str(int(n)) + '^1')
    else:
        print()


n = int(input())
while n > 0:
    n -= 1
    t = int(input())
    prime(t)
