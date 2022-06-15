import array
n = int(input())
s = input()
x = s.split()
count = 0


a = array.array('i')
for i in x:
    a.append(int(i))
for i in range(0, n - 1, 1):
    for j in range(i, n, 1):
        if a[i] > a[j]:
            count += 1
print(count)
