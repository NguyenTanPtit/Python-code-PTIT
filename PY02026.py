# tập hợp số bằng nhau
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = list(set(a))
b = list(set(b))
a.sort()
b.sort()
check = True
if len(a) != len(b):
    check = False
    print('NO')
else:
    for i in a:
        if i not in b:
            check = False
            break
    if not check:
        print('NO')
if check:
    print('YES')
