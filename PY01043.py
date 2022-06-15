# số thuận nghịch chẵn
def checkthuannghich(n):
    s = str(n)
    if s == s[::-1]:
        return True
    return False


def checksochan(n):
    s = str(n)
    for i in s:
        if int(i) % 2 != 0:
            return False
    return True


def checkdodai(n):
    s = str(n)
    if len(s) % 2 == 0:
        return True
    return False


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    for i in range(22, n, 22):
        if checkdodai(i) and checksochan(i) and checkthuannghich(i):
            print(i, end=" ")
    print()
