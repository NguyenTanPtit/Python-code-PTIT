# TÍNH ĐIỂM TRUNG BÌNH
t = int(input())
s = list(map(float, input().split()))
s.sort()
min = s[0]
max = s[len(s)-1]
sum = 0
count = 0
for i in s:
    if i != min and i != max:
        sum += i
        count += 1
print(str(format(float(sum / count),'.2f')))
