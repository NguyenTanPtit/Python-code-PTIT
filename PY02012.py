# sắp xếp chẵn lẻ
t = int(input())
s = []
while len(s) < t:
    s += (list(map(int, input().split())))
chan = []
le = []
for i in s:
    if i % 2 == 0:
        chan.append(i)
    else:
        le.append(i)
chan.sort()
le.sort(reverse=True)
for i in s:
    if i % 2 == 0:
        print(chan[0], end=" ")
        chan.remove(chan[0])
    else:
        print(le[0], end=" ")
        le.remove(le[0])
