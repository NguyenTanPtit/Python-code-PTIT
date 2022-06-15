# biến đổi về dãy bằng nhau
t = int(input())
s = list(map(int, input().split()))
min = 999999999999999999
k = 0
for i in s:
    step = 0
    for j in s:
        step += abs(i - j)
    if step < min:
        min = step
        k = i
print(str(min)+' '+str(k))

