# số lộc phát đẹp
s = input()
check = True
if s[0] == '8':
    check = False
elif '888' in s:
    check = False
else:
    for i in s:
        if i != '6' and i != '8':
            check = False
            break
if check:
    print('YES')
else:
    print('NO')
