# tính tổng các chữ số
t = int(input())
while t > 0:
    t -= 1
    s = input()
    sum = 0
    res = []
    for i in range(len(s)):
        if s[i].isnumeric():
            sum += int(s[i])
        else:
            res.append(s[i])
    res.sort()
    for i in res:
        print(i, end='')
    print(sum)
