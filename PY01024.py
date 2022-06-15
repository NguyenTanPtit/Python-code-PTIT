def chiaHet(n):
    sums = 0
    s = str(n)
    for i in s:
        sums += int(i)
    if sums % 10 == 0:
        return True
    else:
        return False


def check2DV(n):
    s = str(n)
    for i in range(len(s) - 1):
        if abs(int(s[i]) - int(s[i + 1])) - 2 != 0:
            return False
    return True


n = int(input())
while n > 0:
    t = int(input())
    n -= 1
    if chiaHet(t) and check2DV(t):
        print("YES")
    else:
        print("NO")
