P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    s = input().split()
    if s[0] == '0':
        break
    res = ''
    for i in s[1]:
        h = (int(s[0]) + P.index(i)) % 28
        res += P[h]
    t = list(res)
    t.reverse()
    k = ''.join(t)
    print(k)
