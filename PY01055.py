# số xen kẽ
def checkLen(n):
    s = str(n)
    if len(s) % 2==0:
        return False
    else:
        return True


def checkDiff(n):
    s = str(n)
    if s[0] == s[1]:
        return False
    else:
        return True


def check3(n):
    s = str(n)
    a = s[0]
    for i in range(2, len(s), 2):
        if a != s[i]:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if check3(n) and checkDiff(n) and checkLen(n):
        print("YES")
    else:
        print("NO")

