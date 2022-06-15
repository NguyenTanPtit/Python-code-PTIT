# tổng chữ số
s = input()
count = 0
while len(s) > 1:
    res = 0
    for i in s:
        res += ord(i) - ord('0')
    s = str(res)
    count += 1
print(str(count))
