# lớn nhất và nhỏ nhất
while True:
    n = int(input())
    if n == 0:
        break
    else:
        s = []
        while n > 0:
            n -= 1
            s.append(int(input()))
        s.sort()
        if s[0] == s[len(s)-1]:
            print('BANG NHAU')
        else:
            print(str(s[0])+' '+str(s[len(s)-1]))
