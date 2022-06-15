# chèn xâu
s1 = input()
s2 = input()
p = int(input())
res = [s1[:p-1], s2, s1[p-1:]]
for i in res:
    print(i, end='')
