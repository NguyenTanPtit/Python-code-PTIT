# địa chỉ ip
def check(n):
    if len(n) != 4:
        return False
    for i in n:
        if i > '255':
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    a = input()
    s = a.count(".")
    a = a.split(".")
    if s != 3:
        print('NO')
        continue
    if check(a):
        print("YES")
    else:
        print("NO")
