t = int(input())
s = list(map(int, input().split()))
s.sort()
count = 0
for i in range(1, t + 1):
    if i not in s:
        print(i)
        count = 1
        break
if count == 0:
    print(t + 1)
