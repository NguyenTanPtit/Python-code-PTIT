# hệ cơ số 8
s = input()
res = ''
mod = len(s) % 3
for i in range(3 - mod):
    s = '0' + s
for i in range(0, len(s), 3):
    res += str(int(s[i:i + 3], 2))
print(str(int(res)))
